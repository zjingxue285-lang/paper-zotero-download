import importlib.util
import tempfile
import unittest
from pathlib import Path

from reportlab.pdfgen.canvas import Canvas

spec = importlib.util.spec_from_file_location(
    "verify_pdf", Path(__file__).parents[1] / "scripts" / "verify_pdf.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class VerifyPdfTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "example.pdf"
        canvas = Canvas(str(self.path))
        canvas.drawString(40, 700, "Exercise and attention: an example study")
        canvas.drawString(40, 670, "doi:10.1234/example.2026")
        canvas.showPage()
        canvas.save()

    def test_matching_identity(self):
        result = module.inspect_pdf(
            self.path, "https://doi.org/10.1234/example.2026",
            "Exercise and attention: an example study",
        )
        self.assertEqual(result["status"], "identity_verified")
        self.assertEqual(result["pages"], 1)

    def test_wrong_doi_needs_review(self):
        result = module.inspect_pdf(self.path, "10.1234/other", "Exercise and attention")
        self.assertEqual(result["status"], "identity_review")
        self.assertFalse(result["doi_match_on_opening_pages"])

    def test_wrong_title_needs_review(self):
        result = module.inspect_pdf(self.path, "10.1234/example.2026", "Unrelated paper")
        self.assertEqual(result["status"], "identity_review")
        self.assertFalse(result["title_match_on_opening_pages"])

    def test_doi_prefix_is_not_identity(self):
        result = module.inspect_pdf(self.path, "10.1234/example", "Exercise and attention")
        self.assertEqual(result["status"], "identity_review")
        self.assertFalse(result["doi_match_on_opening_pages"])

    def test_html_rejected(self):
        self.path.write_text("<!DOCTYPE html><title>Access denied</title>")
        with self.assertRaises(ValueError):
            module.inspect_pdf(self.path, "10.1234/example.2026", "Exercise")

    def test_empty_expectation_rejected(self):
        with self.assertRaises(ValueError):
            module.inspect_pdf(self.path, "", "Exercise")


if __name__ == "__main__":
    unittest.main()
