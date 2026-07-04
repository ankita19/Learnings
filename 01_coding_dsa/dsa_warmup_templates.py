"""DSA warm-up templates in one class.

This file keeps interview-ready snippets compact and readable.
"""

from __future__ import annotations

from collections import Counter, deque
import heapq


class DSAWarmupTemplates:
    """Single class containing common DSA warm-up patterns."""

    @staticmethod
    def iterate_arrays_and_lists(values: list[int]) -> dict[str, list[int]]:
        """Show common iteration patterns over arrays/lists."""
        forward = [value for value in values]
        backward = [values[i] for i in range(len(values) - 1, -1, -1)]
        indexed_sum = [i + value for i, value in enumerate(values)]
        return {
            "forward": forward,
            "backward": backward,
            "indexed_sum": indexed_sum,
        }

    @staticmethod
    def hashmap_frequency_count(values: list[int]) -> dict[int, int]:
        """Frequency counting using HashMap-style dictionary."""
        return dict(Counter(values))

    @staticmethod
    def hashset_usage(values: list[int], target: int) -> dict[str, object]:
        """Typical HashSet operations: dedupe and O(1)-average membership check."""
        seen = set(values)
        return {
            "unique_values": seen,
            "contains_target": target in seen,
        }

    @staticmethod
    def queue_and_stack_ops(values: list[int]) -> dict[str, list[int]]:
        """Queue (FIFO) and stack (LIFO) examples."""
        queue = deque(values)
        stack = list(values)

        queue_order = []
        while queue:
            queue_order.append(queue.popleft())

        stack_order = []
        while stack:
            stack_order.append(stack.pop())

        return {
            "queue_order": queue_order,
            "stack_order": stack_order,
        }

    @staticmethod
    def priority_queue_min_max(values: list[int]) -> dict[str, list[int]]:
        """Min-heap and max-heap behavior using heapq."""
        min_heap = list(values)
        heapq.heapify(min_heap)

        max_heap = [-value for value in values]
        heapq.heapify(max_heap)

        min_order = [heapq.heappop(min_heap) for _ in range(len(min_heap))]
        max_order = [-heapq.heappop(max_heap) for _ in range(len(max_heap))]

        return {
            "min_heap_order": min_order,
            "max_heap_order": max_order,
        }

    @staticmethod
    def binary_search_template(sorted_values: list[int], target: int) -> int:
        """Standard binary search template. Returns index or -1."""
        left, right = 0, len(sorted_values) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if sorted_values[mid] == target:
                return mid
            if sorted_values[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    @staticmethod
    def dfs_template(graph: dict[str, list[str]], start: str) -> list[str]:
        """Iterative DFS template for adjacency-list graph."""
        visited: set[str] = set()
        order: list[str] = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)

            # Reverse push keeps left-to-right traversal stable.
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

        return order

    @staticmethod
    def bfs_template(graph: dict[str, list[str]], start: str) -> list[str]:
        """BFS template for adjacency-list graph."""
        visited: set[str] = {start}
        order: list[str] = []
        queue = deque([start])

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order


if __name__ == "__main__":
    sample_values = [4, 1, 4, 2, 3]
    sample_sorted = [1, 2, 3, 4, 5, 7, 9]
    sample_graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }

    warmup = DSAWarmupTemplates()

    print("iterate_arrays_and_lists:", warmup.iterate_arrays_and_lists(sample_values))
    print("hashmap_frequency_count:", warmup.hashmap_frequency_count(sample_values))
    print("hashset_usage:", warmup.hashset_usage(sample_values, target=2))
    print("queue_and_stack_ops:", warmup.queue_and_stack_ops(sample_values))
    print("priority_queue_min_max:", warmup.priority_queue_min_max(sample_values))
    print("binary_search_template:", warmup.binary_search_template(sample_sorted, target=7))
    print("dfs_template:", warmup.dfs_template(sample_graph, start="A"))
    print("bfs_template:", warmup.bfs_template(sample_graph, start="A"))
