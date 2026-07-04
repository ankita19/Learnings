"""Utilities for reversing characters inside words while preserving spaces.

Example:
    input:  "  hello  world "
    output: "  olleh  dlrow "
"""

from typing import List


def reverse_words(s: str) -> str:
    """Reverse characters of each word in `s`, preserving exact spaces.

    A word is a contiguous run of non-space characters. All spaces remain
    at their original indices; only characters inside words are reversed.
    """
    chars: List[str] = list(s)
    n = len(chars)
    i = 0
    while i < n:
        if chars[i] == ' ':
            i += 1
            continue
        j = i
        while j < n and chars[j] != ' ':
            j += 1
        # reverse the word in-place between i and j-1
        l, r = i, j - 1
        while l < r:
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        i = j
    return ''.join(chars)

def reverse_words_alternative(s: str) -> str:
    """Alternative implementation using split and join."""
    words = s.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def reverse_words_preserve_spaces_regex(s: str) -> str:
    import re
    parts = re.split(r'(\s+)', s)
    reversed_parts = [p for p in parts if not p.isspace()][::-1]
    return ' '.join(reversed_parts)