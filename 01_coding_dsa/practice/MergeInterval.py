import unittest


def merge_intervals(intervals):
    """
    Merge overlapping intervals in O(N log N) time and O(N) space.
    """
    if not intervals:
        return []

    # 1. Sort by start time - Essential for the single-pass logic
    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        # 2. If merged is empty or no overlap with the last merged interval
        # (Current start is greater than the last merged end)
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # 3. There is an overlap, merge by updating the end of the last interval
            # We take the max of the current end and the last merged end
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


class TestMergeIntervals(unittest.TestCase):
    def test_no_overlap(self):
        self.assertEqual(merge_intervals([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_touching_edge(self):
        # Case where [1, 2] and [2, 4] should become [1, 4]
        self.assertEqual(merge_intervals([[1, 2], [2, 4]]), [[1, 4]])

    def test_overlapping(self):
        self.assertEqual(merge_intervals([[1, 4], [2, 3]]), [[1, 4]])
        self.assertEqual(merge_intervals([[2, 6], [1, 3], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])


if __name__ == "__main__":
    unittest.main()