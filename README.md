# RNIPlanner sample data

Public template samples for developing and trying [RNIPlanner](https://github.com/Alant-Health/RNIPlanner). Image files are distributed as versioned GitHub release assets; this repository stores manifests, provenance, license notices, and contributed landmarks.

## Rebuild or update a bundle

The [download descriptor](descriptors/MNI2009c-v2.json) records the versioned ZIP URL and SHA-256 used by the application. Changes to any artifact or manifest require a new release and descriptor.

To reproduce the ZIP from the checked-in metadata and an extracted release's `artifacts` directory:

```sh
python3 tools/build_bundle.py \
  --dataset datasets/MNI2009c/v2 \
  --artifacts /path/to/MNI2009c/artifacts \
  --output build/MNI2009c-v2.zip
```
