"""Package prepared artifacts with versioned metadata and verify their hashes."""

import argparse
import hashlib
import json
import shutil
import tempfile
import zipfile
from datetime import date
from pathlib import Path


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def build(dataset, artifacts, output):
    manifest = json.loads((dataset / 'template.json').read_text())
    provenance = json.loads((dataset / 'provenance/bundle-provenance.json').read_text())
    stamp = date.fromisoformat(provenance['prepared_date'])
    with tempfile.TemporaryDirectory(prefix='rniplanner-sample-') as directory:
        bundle = Path(directory) / manifest['id']
        shutil.copytree(dataset, bundle)
        for artifact in manifest['artifacts']:
            target = bundle / artifact['path']
            if not target.resolve().is_relative_to(bundle):
                raise ValueError('Artifact paths must stay inside the template folder.')
            if not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(artifacts / Path(artifact['path']).name, target)
            if sha256(target) != artifact['sha256']:
                raise ValueError(f"Artifact checksum mismatch: {artifact['id']}")
        files = sorted(path for path in bundle.rglob('*') if path.is_file() and path.name != 'SHA256SUMS')
        (bundle / 'SHA256SUMS').write_text(''.join(
            f'{sha256(path)}  {path.relative_to(bundle).as_posix()}\n' for path in files
        ))
        output.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_STORED) as archive:
            for path in sorted(path for path in bundle.rglob('*') if path.is_file()):
                info = zipfile.ZipInfo(path.relative_to(bundle.parent).as_posix(),
                                       date_time=(stamp.year, stamp.month, stamp.day, 0, 0, 0))
                info.external_attr = 0o644 << 16
                archive.writestr(info, path.read_bytes())
    print(f'{sha256(output)}  {output}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dataset', type=Path, required=True)
    parser.add_argument('--artifacts', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    build(args.dataset, args.artifacts, args.output)
