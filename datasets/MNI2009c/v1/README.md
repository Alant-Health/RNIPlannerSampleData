# MNI2009c template sample, version 1

Open `template.json` with RNIPlanner's template importer. The bundle contains six scalar images, four label artifacts, and one fiducial point list in the MNI ICBM152 nonlinear asymmetric 2009c space.

T1w is the initial registration image. T2w and PD are intensity artifacts that can be designated as additional registration images in Edit template. Gray matter, white matter, and CSF are probability images carried with the template. Brain, face, and eye label artifacts are eligible masks; the MIAL67 thalamic atlas has 14 named labels. The six landmarks are manually placed AC, PC, M1, M2, M3, and M4 points supplied for development.

All volume grids are 193 x 229 x 193 at 1 mm spacing. Masks were normalized to binary values from the upstream stored labels without changing geometry. Other image data and landmark coordinates are unchanged. `provenance/` records source URLs, hashes, and conversions; `SHA256SUMS` covers the bundle files.

## Attribution and licenses

- MNI ICBM152 2009c: Louis Collins and the McConnell Brain Imaging Centre, Montreal Neurological Institute, McGill University. Original notice: `licenses/MNI-COPYING.txt`. Source: https://www.bic.mni.mcgill.ca/ServicesAtlases/ICBM152NLin2009. Cite Fonov et al. (2011), doi:10.1016/j.neuroimage.2010.07.033, and Fonov et al. (2009), doi:10.1016/S1053-8119(09)70884-5.
- MIAL67: Najdenovska et al., *In-vivo probabilistic atlas of human thalamic nuclei based on diffusion weighted magnetic resonance imaging*, Scientific Data (2018), doi:10.1038/sdata.2018.270. Distributed by TemplateFlow under CC BY 4.0; original authors, curators, and references are retained in the adjacent metadata. License: `licenses/CC-BY-4.0.txt`.
- Landmarks: contributed testing annotations, dedicated to the public domain under CC0 1.0 Universal with no attribution requirement; see `licenses/LANDMARKS.txt` and `licenses/CC0-1.0.txt`.

These landmarks have not been validated by a clinical expert. They are intended for testing and may be replaced with clinician-created points in a later sample version.

This sample contains no patient dataset or patient-derived result.
