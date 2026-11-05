# WasteWave

A real-world microwave reflection dataset for waste material classification.

**Repository status: publication template. Dataset files are not included.**
Only the authors' research manuscript was supplied when preparing this template.
The manuscript itself is not redistributed in this repository. No dataset download,
DOI, release, benchmark implementation, or license is claimed to exist here.

## Dataset described in the manuscript

| Property | Manuscript specification |
|---|---|
| Measurements | 1,112 |
| Unique physical waste items | 97 |
| Metal measurements | 373 |
| Plastic measurements | 375 |
| Cardboard measurements | 364 |
| Frequency span | 863–879 MHz |
| Instrument | nanoVNA-F V2 |
| Antennas | Two Laird Technologies S8655PR directional antennas |
| Recorded parameters | Complex S11 and S21, each with real and imaginary components |
| Instrument sweep | 101 evenly spaced frequency points |

Sources: supplied manuscript, sections 3.2.1, 3.2.2, 3.3 and Table 1.
Counts describe the manuscript, not files verified in this repository.
Four scalar features per frequency and a 101-point sweep imply 404 scalar signal
values per complete sweep; the actual exported shape and ordering must be confirmed.
S-parameters are dimensionless complex ratios; do not assume exported values are dB.
The nominal antenna specification (865–870 MHz) differs from the measurement span;
the manuscript reports testing antennas across 863–879 MHz.

## Layout

```text
data/
  raw/             original exports; empty
  processed/       documented derived data; empty
  metadata/        manifest and proposed schema
  splits/          item/group split assignments; empty
metadata/          machine-readable dataset description
scripts/           file checksum utility
references/        manuscript reference and provenance
docs/              publication, license and data-format instructions
```

## Obtain and use data

No measurement files are available in this template. After a real release, the
maintainer must add a verified download URL, version, license, file checksums,
and loading instructions here. Do not interpret the empty manifest as the dataset.

Preserve physical `item_id` values. For unseen-object evaluation, keep all
measurements of one item within a single train/validation/test partition. Fit
normalization on training data only. Random measurement splits can share items
and answer a different evaluation question (manuscript section 3.7).
No split files, training code or reproduced results are included.

## Publication steps

1. Follow [the Finnish publication guide](docs/JULKAISU.md).
2. Add real files and describe their format using [the proposed schema](docs/DATA_FORMAT.md).
3. Complete [metadata](metadata/dataset.json), including creators and missing identifiers.
4. Choose licenses using [the license guide](docs/LICENSE_SELECTION.md).
5. Validate counts, checksums and item-separated splits before a dataset release.

## Citation

Joona Helenius, Pouya Jafarzadeh, Fahimeh Farahnakian, and Jukka Heikkonen.
*WasteWave: A Real-World Microwave Reflection Dataset and Neural Network-Based
Waste Material Classification*. University of Turku.

Publication year, venue, DOI and dataset DOI must be confirmed by the authors.
A citation file is intentionally omitted until these fields and the dataset release
identifier are confirmed. Do not invent a DOI or use a placeholder as a real URL.

## License

Dataset and repository code/documentation licenses are **not yet selected**.
No permission to reuse data or code is granted by this template. Replace this
notice with the chosen license statements and full license texts before release.
