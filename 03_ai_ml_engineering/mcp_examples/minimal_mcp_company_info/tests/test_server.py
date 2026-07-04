import unittest

from minimal_mcp_company_info.server import get_company_info


class TestGetCompanyInfo(unittest.TestCase):
    def test_known_company(self) -> None:
        result = get_company_info("Teradata")
        self.assertTrue(result["found"])
        self.assertEqual(result["name"], "Teradata")

    def test_unknown_company(self) -> None:
        result = get_company_info("Acme")
        self.assertFalse(result["found"])
        self.assertEqual(result["industry"], "Unknown")

    def test_empty_company_name_raises(self) -> None:
        with self.assertRaises(ValueError):
            get_company_info("   ")


if __name__ == "__main__":
    unittest.main()
