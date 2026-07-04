# pytest tests for sliding window: longest substring without repeating characters
# Save your solution in a file named `solution.py` with functions:
#   - length_of_longest_substring(s: str) -> int
#   - longest_substring_without_repeat(s: str) -> str
# Then run:  pytest -q

import pytest

# Attempt to import user's solution; gracefully skip tests if not present yet.
try:
    from src.sliding_window import length_of_longest_substring, longest_substring_without_repeat
    _IMPORT_ERROR = None
except Exception as e:  # pragma: no cover
    length_of_longest_substring = None  # type: ignore
    longest_substring_without_repeat = None  # type: ignore
    _IMPORT_ERROR = e

pytestmark = pytest.mark.skipif(
    length_of_longest_substring is None or longest_substring_without_repeat is None,
    reason=f"Cannot import required functions from solution.py: {_IMPORT_ERROR}"
)


def brute_force_len(s: str) -> int:
    """O(n^2) brute force to validate results on small strings."""
    n = len(s)
    best = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", 0),
        ("a", 1),
        ("bbbbb", 1),
        ("abcabcbb", 3),          # "abc"
        ("pwwkew", 3),            # "wke"
        ("dvdf", 3),              # "vdf"
        ("abba", 2),              # "ab" or "ba"
        ("tmmzuxt", 5),           # "mzuxt"
        ("anviaj", 5),            # "nviaj"
        ("😀😃😄😀", 3),           # emoji unicode
        ("中文测试中文", 4),          # unicode CJK
    ],
)
def test_length_examples(s, expected):
    assert length_of_longest_substring(s) == expected


def test_substring_properties_examples():
    cases = [
        "", "a", "bbbbb", "abcabcbb", "pwwkew", "dvdf", "abba", "tmmzuxt", "anviaj", "😀😃😄😀", "中文测试中文"
    ]
    for s in cases:
        sub = longest_substring_without_repeat(s)
        # substring must actually be a substring of s
        assert s.find(sub) != -1
        # must have all unique characters
        assert len(set(sub)) == len(sub)
        # its length must match the length function
        assert len(sub) == length_of_longest_substring(s)


def test_random_small_against_bruteforce():
    import random
    random.seed(1337)
    alphabet = "abcde"
    for _ in range(200):
        n = random.randint(0, 8)
        s = "".join(random.choice(alphabet) for _ in range(n))
        assert length_of_longest_substring(s) == brute_force_len(s)

