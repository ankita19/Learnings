import unittest

from app import handle_user_prompt, handle_user_prompt_with_mock_llm, route_user_prompt


class TestUserCallPoc(unittest.TestCase):
    def test_route_to_tool(self) -> None:
        tool_call = route_user_prompt("get me Teradata company info")
        self.assertEqual(tool_call.name, "get_company_info")
        self.assertEqual(tool_call.arguments["company_name"], "teradata")

    def test_handle_known_company(self) -> None:
        result = handle_user_prompt("get me Teradata company info")
        self.assertTrue(result["found"])
        self.assertEqual(result["name"], "Teradata")

    def test_handle_unknown_company(self) -> None:
        result = handle_user_prompt("get me Acme company info")
        self.assertFalse(result["found"])
        self.assertEqual(result["industry"], "Unknown")

    def test_mock_llm_path(self) -> None:
        result = handle_user_prompt_with_mock_llm("get me Teradata company info")
        self.assertFalse(result["needs_clarification"])
        self.assertEqual(result["tool_used"], "get_company_info")
        self.assertTrue(result["result"]["found"])
        self.assertEqual(result["result"]["name"], "Teradata")

    def test_mock_llm_clarification_path(self) -> None:
        result = handle_user_prompt_with_mock_llm("hello there")
        self.assertTrue(result["needs_clarification"])
        self.assertIn("company info", result["message"].lower())


if __name__ == "__main__":
    unittest.main()
