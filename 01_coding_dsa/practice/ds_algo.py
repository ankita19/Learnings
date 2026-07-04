# sliding window - longet substring

def LongestSubstringWithUnique(s: str) -> str:
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



