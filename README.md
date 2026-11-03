# Paper Zotero Download

A reusable agent skill for finding legally accessible paper PDFs, verifying their identity, and attaching them to **existing** Zotero items. Designed around Windows/Edge workflows without macOS AppleScript dependencies.

## What It Does

- Prioritizes open-access publisher and repository copies.
- Skips CAPTCHA/security verification instead of repeatedly trying to bypass it.
- Preserves original Zotero metadata, tags, notes and collection membership.
- Checks title, DOI, PDF readability and page count before attachment.
- Prefers stored attachments and records resumable per-paper outcomes.
- Distinguishes journal papers, conference abstracts and preprints.

This is an agent workflow plus a PDF validator, **not** a one-click Zotero plugin or an unattended browser downloader. Your agent needs supported file-download and Zotero interaction tools. Browser automation and institutional access depend on the environment; no success rate is guaranteed.

## Install as a Skill

Copy this repository's skill folder (including `SKILL.md`, `references/` and `scripts/`) into your agent's skills directory under `paper-zotero-download`. For Codex, the usual directory is `~/.codex/skills/`. Follow your client's skill discovery/reload behavior.

Example request:

> Use paper-zotero-download to retrieve PDFs for this Zotero collection. Start with three items. Skip sites requiring verification, preserve my tags and attach to the existing records.

## Optional PDF Validator

Requires Python and `pypdf`:

```sh
python -m pip install pypdf
python scripts/verify_pdf.py paper.pdf --doi 10.1234/example --title "Expected title"
```

Exit codes: `0` identity verified; `2` manual identity review needed; `1` invalid/unreadable input. It does not judge scientific eligibility or publication type. Do not discard records simply because text extraction fails.

Tests additionally need `reportlab`:

```sh
python -m pip install reportlab
python -m unittest discover -s tests -v
```

## Privacy

Keep downloaded papers, library exports, credentials and acquisition logs outside this repository. Publishing the skill never implies permission to publish research files or library contents.

## Acknowledgment

Inspired by the workflow in [operoncao123/browser-paper-download](https://github.com/operoncao123/browser-paper-download). The helper code here is independently written; no AppleScript or CAPTCHA-solving implementation is included.

License: MIT.
