---
name: paper-zotero-download
description: Find legally accessible paper PDFs, verify their identity, and attach them to existing Zotero items without duplicates. Use for individual or batch full-text retrieval, including Windows with Edge. Skip verification-blocked sites and record resumable progress. Not a literature-screening skill.
---

# Paper PDFs to Existing Zotero Items

## Scope

Retrieve PDFs for the user's specified collection or list. A download is not evidence of eligibility for a systematic review. Preserve the existing bibliography, original subject tags, screening tags, notes, and collection membership.

This is an agent workflow, not a Zotero plugin or unattended browser driver. It requires tools for downloading files and operating Zotero, plus Python and `pypdf` for the optional validator. Do not claim attachment capability until a supported interface has been observed. Read the environment's computer-use instructions before controlling apps.

## Efficient Workflow

1. Identify the exact collection and parent item by title, author/year and DOI. Check for an existing matching PDF before downloading. Multiple imported collections may contain distinct copies of the same paper; target the user-selected item, not an arbitrary global match.
2. Start with a small pilot (normally 3 items) when the interface or download route is untested. Do not extrapolate pilot success to the entire batch.
3. Prefer a publicly accessible publisher PDF, PMC/Europe PMC, or a trustworthy institutional repository. Resolve metadata using DOI/PMID; do not invent missing identifiers or silently select the nearest title match.
4. For public direct URLs, use an available download tool first. For institutional access, use the user's already authenticated browser through the supported browser/computer interface. Do not assume command-line downloads inherit browser access.
5. If a CAPTCHA, security verification, login wall, or browser safety interstitial appears, record the actual blocker and move to another known lawful source or the next paper. Do not solve, bypass, repeatedly reload, extract cookies, or request passwords. Close only a temporary tab opened by this workflow; preserve pre-existing user tabs. A failed browser-control safety check is a tool blocker: stop that UI route rather than substituting another automation technology.
6. Verify the file before attachment. HTTP success, a `.pdf` suffix, or `%PDF-` alone is insufficient. Run the helper or equivalent checks: parseable PDF, page count, expected title and DOI on opening pages, author/year, and publication type. Read the opening page if extraction is incomplete. Reject HTML disguised as PDF and mismatched articles; do not attach unverified candidates.
7. Attach the verified PDF to the existing parent item using a supported Zotero API or observed UI. Do not import another RIS or create a second parent. Prefer a stored file, not a link to a temporary download. For UI-specific details read [references/zotero-ui.md](references/zotero-ui.md).
8. Verify both parent-child placement in Zotero and file readability. Where available compare the stored PDF's hash to the verified download. An attachment icon alone does not prove the correct paper was saved.
9. Update a local progress file after each item. Resume from it, but recheck that a previously attached file still exists. Report verified attachments, unresolved items and explicit blockers separately. Never call a queued or stalled operation complete.

## Validation Helper

```text
python scripts/verify_pdf.py downloaded.pdf --doi 10.1234/example --title "Expected title"
```

The helper prints JSON to stdout and exits 0 only when both DOI and title match on the first two pages. Exit 2 means human review is needed; exit 1 means the file cannot be validated. This is a deliberately strict identity check, not a scientific eligibility or publication-type classifier. False negatives are possible with scanned PDFs, translated titles, or unusual layouts. Missing DOI is not proof of mismatch; review manually instead of discarding the record.

## Progress Fields

Keep a private JSONL/CSV log outside the installed skill and public repository:

`record_id`, `collection`, `title`, `doi`, `source_url`, `status`, `reason`, `pages`, `sha256`, `attachment_id_or_path`, `verified_at`.

Use stable statuses:
- `attached_verified`: identity and existing-parent placement verified.
- `already_attached_verified`: matching existing attachment verified.
- `downloaded_not_attached`: verified PDF exists, attachment pending.
- `identity_review`: ambiguous metadata or incomplete text extraction.
- `blocked_verification`: CAPTCHA or security challenge.
- `needs_user_login`: authentication required.
- `no_access`: explicit access/subscription restriction.
- `not_found`: searched routes produced no candidate; not proof no full text exists.
- `tool_blocked`: app/browser interface unavailable or unsafe to control.

Record document type separately: `journal_article`, `conference_abstract`, `preprint`, `correction`, or `unknown`. Do not label a 2-page poster abstract as a complete study paper. If a related formal publication is found, record the relationship for review; do not silently replace the original record or assert identical samples.

## Batch Limits and Token Use

Save successful route patterns and new reproducible failure modes in the relevant reference; keep per-paper results in the progress log, not the skill. Avoid repeated full accessibility trees, screenshots of unchanged states, or rereading scripts. Use compact state excerpts after observations, but always refresh state before UI actions. Stop the current item after one attempt per known route and at most one evidence-based fallback unless the user requests deeper tracing. Ask before extending a pilot into a long batch when authorization only covered the pilot.

## Publication Hygiene

Publishing or updating this skill requires explicit user intent. Upload only reusable instructions, original helper code, tests and documentation. Never include downloaded papers, personal paths, collection exports, screening notes, credentials, browser profiles or acquisition logs. Do not add every completed batch as a new skill.

## Sources and Limitations

Workflow inspiration: [browser-paper-download](https://github.com/operoncao123/browser-paper-download). Its AppleScript downloader is macOS-specific and is not used here. No CAPTCHA-solving procedures are adopted. This skill does not promise universal Windows/browser/publisher compatibility.

Zotero attachment behavior: [official documentation](https://www.zotero.org/support/attaching_files).
