"""Vote Counter - Atlassian Interview Question

Problem: Given a list of votes for candidates, determine the winner based on
the total number of votes for each candidate.

Example: ['c1', 'c2', 'c1', 'c2', 'c1', 'c2', 'c3', 'c4', 'c4']
Expected: c1 or c2 (both have 3 votes - need to handle ties)
"""

from typing import List, Optional, Dict, Set
from collections import Counter


def find_winner_basic(votes: List[str]) -> Optional[str]:
    """Basic approach using Counter - most Pythonic and clean.

    Time Complexity: O(n) where n is the number of votes
    Space Complexity: O(k) where k is the number of unique candidates

    Args:
        votes: List of candidate identifiers

    Returns:
        The candidate with the most votes, or None if votes is empty

    Note: Returns first candidate encountered in case of tie
    """
    if not votes:
        return None

    vote_counts = Counter(votes)
    return vote_counts.most_common(1)[0][0]


def find_winner_with_tie_detection(votes: List[str]) -> Dict[str, any]:
    """Production-ready version with tie detection and detailed results.

    Time Complexity: O(n)
    Space Complexity: O(k)

    Returns:
        Dictionary with:
        - winner: candidate(s) with most votes
        - vote_count: number of votes winner(s) received
        - is_tie: whether there was a tie
        - all_results: complete vote breakdown
    """
    if not votes:
        return {
            'winner': None,
            'vote_count': 0,
            'is_tie': False,
            'all_results': {}
        }

    vote_counts = Counter(votes)
    max_votes = max(vote_counts.values())

    # Find all candidates with max votes (handles ties)
    winners = [candidate for candidate, count in vote_counts.items()
               if count == max_votes]

    return {
        'winner': winners[0] if len(winners) == 1 else winners,
        'vote_count': max_votes,
        'is_tie': len(winners) > 1,
        'all_results': dict(vote_counts)
    }


def find_winner_manual(votes: List[str]) -> Optional[str]:
    """Manual implementation without Counter - shows algorithmic thinking.

    Useful if interviewer asks you to implement without using Counter.

    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    if not votes:
        return None

    vote_counts: Dict[str, int] = {}

    # Count votes
    for vote in votes:
        vote_counts[vote] = vote_counts.get(vote, 0) + 1

    # Find maximum
    max_candidate = None
    max_votes = 0

    for candidate, count in vote_counts.items():
        if count > max_votes:
            max_votes = count
            max_candidate = candidate

    return max_candidate


def find_winner_streaming(votes: List[str]) -> Optional[str]:
    """Optimized streaming approach - single pass with running max.

    Useful for discussing optimization in interviews.

    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    if not votes:
        return None

    vote_counts: Dict[str, int] = {}
    current_winner = None
    max_votes = 0

    for vote in votes:
        vote_counts[vote] = vote_counts.get(vote, 0) + 1

        # Update winner if this candidate now has more votes
        if vote_counts[vote] > max_votes:
            max_votes = vote_counts[vote]
            current_winner = vote

    return current_winner


def find_top_k_candidates(votes: List[str], k: int = 3) -> List[tuple]:
    """Extension: Find top K candidates - shows thinking beyond the problem.

    Args:
        votes: List of candidate identifiers
        k: Number of top candidates to return

    Returns:
        List of (candidate, vote_count) tuples sorted by vote count descending
    """
    if not votes:
        return []

    vote_counts = Counter(votes)
    return vote_counts.most_common(k)


# Edge Cases and Input Validation

def find_winner_robust(votes: List[str]) -> Dict[str, any]:
    """Production-grade with input validation and error handling.

    Demonstrates defensive programming for senior/principal roles.
    """
    # Input validation
    if votes is None:
        raise ValueError("Votes cannot be None")

    if not isinstance(votes, list):
        raise TypeError(f"Expected list, got {type(votes).__name__}")

    # Filter out invalid votes (None, empty strings)
    valid_votes = [v for v in votes if v and isinstance(v, str)]

    if not valid_votes:
        return {
            'winner': None,
            'vote_count': 0,
            'is_tie': False,
            'all_results': {},
            'invalid_votes': len(votes) - len(valid_votes)
        }

    vote_counts = Counter(valid_votes)
    max_votes = max(vote_counts.values())
    winners = [candidate for candidate, count in vote_counts.items()
               if count == max_votes]

    return {
        'winner': winners[0] if len(winners) == 1 else winners,
        'vote_count': max_votes,
        'is_tie': len(winners) > 1,
        'all_results': dict(vote_counts),
        'invalid_votes': len(votes) - len(valid_votes)
    }


# Example usage and test cases
if __name__ == "__main__":
    # Test case from the problem
    votes = ['c1', 'c2', 'c1', 'c2', 'c1', 'c2', 'c3', 'c4', 'c4']

    print("Basic approach:")
    print(f"Winner: {find_winner_basic(votes)}")
    print()

    print("With tie detection:")
    result = find_winner_with_tie_detection(votes)
    print(f"Result: {result}")
    print()

    print("Manual implementation:")
    print(f"Winner: {find_winner_manual(votes)}")
    print()

    print("Top 3 candidates:")
    print(f"Top K: {find_top_k_candidates(votes, k=3)}")
    print()

    # Edge cases
    print("Edge Cases:")
    print(f"Empty list: {find_winner_basic([])}")
    print(f"Single vote: {find_winner_basic(['c1'])}")
    print(f"All same: {find_winner_basic(['c1', 'c1', 'c1'])}")

    # Tie scenario
    tie_votes = ['c1', 'c1', 'c2', 'c2']
    print(f"\nTie detection: {find_winner_with_tie_detection(tie_votes)}")
