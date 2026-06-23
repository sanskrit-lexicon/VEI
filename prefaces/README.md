# VEI — Front matter (prefaces)

Front-matter OCR of the **Vedic Index of Names and Subjects** by **Arthur Anthony Macdonell** and **Arthur Berriedale Keith**, with a Foreword by Dr. Sampurnanand — published by Motilal Banarsidass, Varanasi (Indian Texts Series), 2 vols. The Preface is signed at Oxford, *July 18, 1912*.

Source scans: Cologne Digital Sanskrit Lexicon
(`https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/dictionaries/prefaces/veipref.html`).

**Source language: English** — the base `veiprefNN.md` files are therefore the English text; there are no separate `.en.md` files. Each page also has a Russian translation `veiprefNN.ru.md`. The tiny Cologne digitizer running header/footer stamps are omitted from each transcription.

## File conventions

| Suffix | Meaning |
|---|---|
| `veiprefNN.md` | Faithful OCR of page NN (source language = English) |
| `veiprefNN.ru.md` | Russian translation of page NN |
| `veipref_all.en.md` | All pages consolidated (English) + table of contents |
| `veipref_all.ru.md` | All pages consolidated (Russian) + table of contents |
| `build_combined.py` | Reproducible builder for the `veipref_all.*` editions (`DICT=vei python build_combined.py`) |
| `scans/vei*.png` | Original Cologne scan pages |

## Consolidated editions

| Language | File |
|---|---|
| English (source) | [veipref_all.en.md](veipref_all.en.md) |
| Russian | [veipref_all.ru.md](veipref_all.ru.md) |

Built by [build_combined.py](build_combined.py).

## Contents

| Page | Section | Vol. | Source | RU |
|---|---|---|---|---|
| 01 | Title | 1 | [veipref01.md](veipref01.md) | [ru](veipref01.ru.md) |
| 02 | Foreword, 1 | 1 | [veipref02.md](veipref02.md) | [ru](veipref02.ru.md) |
| 03 | Foreword, 2 | 1 | [veipref03.md](veipref03.md) | [ru](veipref03.ru.md) |
| 04 | Preface, 1 | 1 | [veipref04.md](veipref04.md) | [ru](veipref04.ru.md) |
| 05 | Preface, 2 | 1 | [veipref05.md](veipref05.md) | [ru](veipref05.ru.md) |
| 06 | Preface, 3 | 1 | [veipref06.md](veipref06.md) | [ru](veipref06.ru.md) |
| 07 | Preface, 4 | 1 | [veipref07.md](veipref07.md) | [ru](veipref07.ru.md) |
| 08 | Preface, 5 | 1 | [veipref08.md](veipref08.md) | [ru](veipref08.ru.md) |
| 09 | Preface, 6 | 1 | [veipref09.md](veipref09.md) | [ru](veipref09.ru.md) |
| 10 | Preface, 7 | 1 | [veipref10.md](veipref10.md) | [ru](veipref10.ru.md) |
| 11 | Preface, 8 | 1 | [veipref11.md](veipref11.md) | [ru](veipref11.ru.md) |
| 12 | Preface, 9 | 1 | [veipref12.md](veipref12.md) | [ru](veipref12.ru.md) |
| 13 | Preface, 10 | 1 | [veipref13.md](veipref13.md) | [ru](veipref13.ru.md) |
| 14 | Preface, 11 | 1 | [veipref14.md](veipref14.md) | [ru](veipref14.ru.md) |
| 15 | Preface, 12 | 1 | [veipref15.md](veipref15.md) | [ru](veipref15.ru.md) |
| 16 | Map of Vedic India | 2 | [veipref16.md](veipref16.md) | [ru](veipref16.ru.md) |

**Signatures / dates found:** Preface signed *A. A. MACDONELL, Oxford, July 18, 1912*. The Foreword (pp. 02–03) is by the Hon'ble Dr. Sampurnanand, Chief Minister, Uttar Pradesh.

**Notes.** Page 16 is the folding "Map of Vedic India" plate (vol. 2): only its title block, legend, scale, and a few representative region labels are transcribed; the geographic detail is not reproducible as text. The Sanskrit alphabet order printed at the foot of the last Preface page (15) is preserved verbatim. Sanskrit terms are kept in IAST with full diacritics as printed.

<details>
<summary><strong>OCR run notes (2026-06-23)</strong> — resume run, source server offline</summary>

Produced by the `/cologne-preface-ocr` skill (vision OCR + translation). Process retrospective, not part of the deliverable.

This was a **resume / disk-only** run: the Cologne scan server was down, so nothing was fetched. All 16 scans (`vei1_Page_545`, `vei1_Page_547`–`560`, `vei2_Page_595`) were already on disk, and all 16 `veiprefNN.md` OCR pages had been completed in earlier sessions. The OCR portion required no new vision work. The gap closed this run was the Russian translations for pages **10–16** (`veipref10.ru.md`–`veipref16.ru.md`); the English base pages are the source text, so no `.en.md` files are needed. The `veipref_all.en.md` and `veipref_all.ru.md` consolidated editions were rebuilt with `build_combined.py` (glob `veipref[0-9][0-9].md` matches the on-disk names — the `veiNN` glob bug did not apply). Verified: 17 H2 headings each (1 TOC + 16 pages), no UTF-8 BOMs.

**Cost.** Synchronous main-thread only, no subagents. Translations 10–16 (7 pages of scholarly prose) ≈ low tens of thousands of output tokens; total run ≈ 80–110k tokens.

**Pending.** None — all 16 toctree pages have a scan and a transcription.

</details>
