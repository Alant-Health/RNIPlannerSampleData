# RNIPlanner sample data

Public template samples for developing and trying [RNIPlanner](https://github.com/Alant-Health/RNIPlanner). Image files are distributed as versioned GitHub release assets; this repository stores manifests, provenance, license notices, and contributed landmarks.

## MNI2009c v1

[Download the release](https://github.com/Alant-Health/RNIPlannerSampleData/releases/tag/mni2009c-v1). The ZIP contains one template in the MNI ICBM152 nonlinear asymmetric 2009c space:

| Artifacts | Role |
| --- | --- |
| T1w | Initial registration image |
| T2w, PD, gray matter, white matter, CSF | Additional intensity images |
| Brain, face, and eye masks | Binary label artifacts eligible as masks |
| MIAL67 thalamic nuclei | Label artifact with 14 named regions |
| AC, PC, and four midsagittal points | Landmark artifact |

The landmarks have not been validated by a clinical expert. They are intended for testing and may be replaced with clinician-created points in a later sample version.

RNIPlanner downloads the ZIP, checks its SHA-256, caches it, and loads the manifest's artifacts through Slicer's native volume, segmentation, and fiducial loaders. For offline use, download the ZIP or extract it and select `MNI2009c/template.json` when creating a template. T2w and PD can be designated as additional registration images through Edit template.

## Sources and licenses

The MNI images retain the [McGill notice](datasets/MNI2009c/v1/licenses/MNI-COPYING.txt). The MIAL67 atlas retains [CC BY 4.0](datasets/MNI2009c/v1/licenses/CC-BY-4.0.txt) and its original attribution. The contributed landmarks use [CC0 1.0](datasets/MNI2009c/v1/licenses/LANDMARKS.txt), with no attribution requirement. These terms are separate; CC0 does not apply to the upstream images or atlas.

See the [dataset README](datasets/MNI2009c/v1/README.md) and [provenance manifest](datasets/MNI2009c/v1/provenance/bundle-provenance.json) for source URLs, references, original hashes, and mask normalization details. No private patient images or patient-derived results are included.

## Rebuild or update a bundle

The [download descriptor](descriptors/MNI2009c-v1.json) records the versioned ZIP URL and SHA-256 used by the application. Changes to any artifact or manifest require a new release and descriptor; do not replace an existing version's assets.

To reproduce the ZIP from the checked-in metadata and an extracted release's `artifacts` directory:

```sh
python3 tools/build_bundle.py \
  --dataset datasets/MNI2009c/v1 \
  --artifacts /path/to/MNI2009c/artifacts \
  --output build/MNI2009c-v1.zip
```

The packager verifies each artifact against its manifest hash, includes the license and provenance files, and writes a deterministic archive. Generating new image content from upstream sources also requires the conversions recorded in the provenance manifest; this script packages already prepared artifacts.
