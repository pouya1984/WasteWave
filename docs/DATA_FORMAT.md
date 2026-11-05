# Proposed data organization — not an observed export schema

The real files were not provided. Retain original exports in `data/raw/` and
record their actual extension, encoding, delimiter, field names, units, missing
values, frequency ordering, calibration and measurement geometry when known.
Do not rename an original export to CSV without converting and documenting it.

For a normalized long-form CSV, this repository proposes:

| Field | Meaning |
|---|---|
| measurement_id | Unique identifier of one orientation/sweep |
| item_id | Stable physical object identifier, shared across its sweeps |
| material | metal, plastic, or cardboard; explicitly map original labels |
| frequency_hz | Frequency in Hz |
| s11_real, s11_imag | Real and imaginary S11 components |
| s21_real, s21_imag | Real and imaginary S21 components |

This is a proposal, not a claim about the dataset's native layout. Do not insert
synthetic rows and present them as original measurements. With 101 points for each
of 1,112 complete sweeps, the proposed long table would contain 112,312 rows;
verify this against actual data rather than imposing it on incomplete exports.

Use a separate item table if item descriptions are available. Use split files
with measurement_id, item_id, partition and fold, documenting seed and algorithm.
No item counts per material, calibration details, acquisition dates, or orientation
angles have been inferred. Units of angle and distance must be supplied by authors.

`data/metadata/manifest.csv` contains only a header. Fill one row per released
file with a repository-relative POSIX path, byte count, SHA-256, role, format and
applicable counts. Leave inapplicable counts blank. Generate hashes with
`python3 scripts/checksums.py` after copying actual files into the data folders.
The utility prints checksums; it does not infer measurement or item counts.
