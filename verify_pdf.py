"""Conservative PDF identity check; no network or Zotero database access."""

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path


def compact(value):
    return "".join(unicodedata.normalize("NFKC", value).lower().split())


def words_only(value):
    return "".join(c for c in compact(value) if c.isalnum())


def inspect_pdf(path, doi, title):
    from pypdf import PdfReader

    path = Path(path)
    if not doi.strip() or not title.strip():
        raise ValueError("Both expected DOI and title must be nonempty")
    data = path.read_bytes()
    if b"%PDF-" not in data[:1024]:
        raise ValueError("Not a PDF header; possibly an HTML error page")
    reader = PdfReader(path)
    if not reader.pages:
        raise ValueError("PDF contains no pages")
    opening = "\n".join(p.extract_text() or "" for p in reader.pages[:2])
    expected_doi = doi.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if expected_doi.lower().startswith(prefix):
            expected_doi = expected_doi[len(prefix):].strip()
            break
    if not expected_doi:
        raise ValueError("Expected DOI is empty after removing its prefix")
    if not re.fullmatch(r"10\.\d{4,9}/\S+", expected_doi, re.IGNORECASE):
        raise ValueError("Expected DOI is not a DOI identifier")
    candidates = re.findall(
        r'10\.\d{4,9}/[^\s<>"\u201c\u201d]+',
        unicodedata.normalize("NFKC", opening),
        flags=re.IGNORECASE,
    )
    doi_match = any(
        expected_doi.lower() in (candidate.lower(), candidate.lower().rstrip(".,;)]}"))
        for candidate in candidates
    )
    title_match = words_only(title) in words_only(opening)
    if not words_only(title):
        raise ValueError("Expected title has no letters or numbers")
    return {
        "status": "identity_verified" if doi_match and title_match else "identity_review",
        "pages": len(reader.pages),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "doi_match_on_opening_pages": doi_match,
        "title_match_on_opening_pages": title_match,
        "note": "Author/year, publication type and Zotero placement need separate review.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--doi", required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    try:
        result = inspect_pdf(args.pdf, args.doi, args.title)
    except Exception as error:
        print(json.dumps({"status": "invalid_or_unreadable", "error": str(error)}))
        return 1
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0 if result["status"] == "identity_verified" else 2


if __name__ == "__main__":
    sys.exit(main())
