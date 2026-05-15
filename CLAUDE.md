# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**VEI** is the repository for processing and correcting the Cologne digitization of Macdonell and Keith's *Vedic Index of Names and Subjects* (1912). It contains the pipeline to generate `vei.xml` from the source text and any corrections.

The canonical source lives in `csl-orig/v02/vei/vei.txt` (and `veihw2.txt`).

## Architecture

| File | Purpose |
|---|---|
| `make_xml.py` | Generates `vei.xml` from the VEI source text and headword file |
| `make_xml.sh` | Shell wrapper for `make_xml.py` |
| `vei.xml` | Generated XML output (tracked by git) |

### XML generation

```bash
# Run from repo root (adjust paths to your installation):
python make_xml.py ../../Cologne_localcopy/vei/veitxt/vei.txt \
  ../../Cologne_localcopy/vei/veixml/xml/veihw2.txt vei.xml
```

Issues and corrections are tracked via the [GitHub issue tracker](https://github.com/sanskrit-lexicon/VEI/issues).

## Dependencies

- **Python 3**
- **vei.txt** — VEI source text
- **veihw2.txt** — VEI headword file
