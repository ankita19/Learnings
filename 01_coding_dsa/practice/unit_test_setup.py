import unittest

# --- STEP 1: YOUR ACTUAL CODE ---
# Pro-tip: Keep your logic in a class or function separate from tests
class RateLimiter:
    def __init__(self):
        self.requests = {}

    def is_allowed(self, user_id):
        # Placeholder logic: allow everyone for now
        # We will implement the real logic once we see the tests fail
        return True


# --- STEP 2: THE UNIT TEST SKELETON ---
class TestRateLimiter(unittest.TestCase):
    
    def setUp(self):
        """
        This runs BEFORE every single test method.
        Use it to reset your objects so tests don't interfere with each other.
        """
        self.limiter = RateLimiter()

    def test_new_user_is_allowed(self):
        """Test names should be descriptive."""
        result = self.limiter.is_allowed("user_1")
        self.assertTrue(result, "New users should be allowed by default")

    def test_multiple_users_are_independent(self):
        """Testing that state for user_1 doesn't affect user_2."""
        self.limiter.is_allowed("user_1")
        self.assertTrue(self.limiter.is_allowed("user_2"))

    # def test_failing_case(self):
    #     """Uncomment this to see what a failure looks like"""
    #     self.assertEqual(1, 2, "This should fail to test your setup")


# --- STEP 3: THE EXECUTION BLOCK ---
if __name__ == "__main__":
    # This magic line runs all the tests defined in classes above
    unittest.main()