from typing import Tuple


def length_of_longest_substring(s: str) -> int:
    """Return the length of the longest substring without repeating characters.

    Uses a sliding-window with a map of last-seen indices for O(n) time and O(min(n,|charset|)) space.
    """
    last_seen: dict[str, int] = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            # move left to one past the previous occurrence
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best


def longest_substring_without_repeat(s: str) -> str:
    known_char = set()
    left = 0
    max_length = 0
    best_start = 0

    for r in range(len(s)):
        while s[r] in known_char:
            known_char.remove(s[left])
            left += 1
        known_char.add(s[r])

        windlow_length = r - left + 1
        if  windlow_length > max_length:
            best_start = left
            max_length = windlow_length

    return s[best_start: best_start + max_length]



__all__ = ["length_of_longest_substring", "longest_substring_without_repeat"]
