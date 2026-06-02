# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**VEI** is the development and correction repository for **A. A. Macdonell and A. B. Keith's *Vedic Index of Names and Subjects***, a specialized index of names and subjects in Vedic literature, within the [Cologne Digital Sanskrit Lexicon](https://www.sanskrit-lexicon.uni-koeln.de/) (CDSL).

- **Canonical source text**: [`csl-orig/v02/vei/vei.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/vei/vei.txt) (3,704 index entries) — corrections are applied to that file, not stored here.
- This repository holds **development artifacts**: corrections, markup, comparison, and per-issue working files.
- An encyclopaedic index of Vedic names and subjects rather than a general dictionary; uses per-page footnote markup.

## Key commands

Corrections follow the CDSL `updateByLine.py` pattern, applied against the csl-orig source:

```sh
python updateByLine.py <input> <changefile> <output>
```

Change-file format (paired lines; `;`-prefixed comments):

```
1234 old <original line>
1234 new <replacement line>
```
Supports `new` (replace), `ins` (insert after), `del` (delete). All files UTF-8 (**no BOM**).

## Data format

VEI entries use standard CDSL Sanskrit-lexicography markup. See [DATA_DICTIONARY.md](DATA_DICTIONARY.md) for the full tag reference.

| Tag | Role |
|---|---|
| `<L>NNNN<pc>PPP` | Entry begin, with print page-column ref |
| `<k1>`, `<k2>` | Primary / secondary headword (SLP1) |
| `<LEND>` | Entry end |
| `{#…#}` | Sanskrit text (SLP1) |
| `{%…%}` | English gloss / italic display text |
| `¦` | Headword / definition separator |
| `<lex>…</lex>` | Lexical category |
| `<ls>…</ls>` | Literary source citation |

Annotated example — the first entry of `vei.txt`:

```
<L>1<pc>1-001<k1>aMSu<k2>aMSu
{@Aṃśu.@}¦ — I. Name of a protégé of the Aśvins in the Rigveda.<sup>1</sup>
2. {@Dhānaṃjayya,@} pupil of {@Amāvāsya Śāṇḍilyāyana,@} according
to the Vaṃśa Brāhmaṇa.<sup>2</sup>
<F>1) viii. 5, 26. {%Cf.%} Ludwig, Transla-
tion of the Rigveda, 3, 160; Hopkins,
{%Journal of the American Oriental Society,%}
17, 89; Sieg, {%Die Sagenstoffe des Ṛgveda,%}
129, suggests that he may be identical
with {@Khela.@}</F>
<F>2) {%Indische Studien,%} 4, 373.</F>
<LEND>
```

## Dependencies

- Python 3 (correction and comparison scripts).
- No build step in this repo; XML and web display are generated centrally from `csl-orig` via `csl-pywork`.

## GitHub Issue Conventions

This repository uses the Cologne dictionary-repo issue taxonomy. Every issue has exactly one **type**, one **severity**, and one **milestone**:

- **Type** (9): link-target, link-splitting, markup, text-correction, content-enhancement, encoding, scan-quality, bug, question
- **Severity** (3): minor, medium, hard
- **Milestone** (4): Dictionary to Book, Digitization Quality, Structured Data, Major Enhancements

See the [Cologne issue runbook](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-issue-runbook.md) for label definitions and the type→milestone mapping.