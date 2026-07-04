"""Interactive practice session for vote counter problem

Run this to practice explaining and coding the solution in interview conditions.
"""

import time
from typing import List, Optional
from collections import Counter


def practice_prompt():
    """Simulate interview question prompt"""
    print("=" * 70)
    print("ATLASSIAN INTERVIEW - PRINCIPAL BACKEND ENGINEER")
    print("=" * 70)
    print()
    print("PROBLEM:")
    print("-" * 70)
    print("Given a list of votes for candidates, determine the winner based on")
    print("the total number of votes for each candidate.")
    print()
    print("Example:")
    print("  Input:  ['c1', 'c2', 'c1', 'c2', 'c1', 'c2', 'c3', 'c4', 'c4']")
    print("  Output: 'c1' or 'c2' (both have 3 votes)")
    print()
    print("-" * 70)
    print()
    input("Press Enter when ready to start (timer will begin)...")
    print()
    return time.time()


def show_checklist():
    """Display interview checklist"""
    print("\n" + "=" * 70)
    print("INTERVIEW CHECKLIST - Did you:")
    print("=" * 70)
    checklist = [
        "1. Ask clarifying questions about ties?",
        "2. Ask about edge cases (empty list, None values)?",
        "3. Discuss the optimal approach before coding?",
        "4. Mention time/space complexity: O(n) time, O(k) space?",
        "5. Write clean, readable code with type hints?",
        "6. Test with example, edge cases, and tie scenarios?",
        "7. Discuss scalability and follow-up questions?",
        "8. Maintain good communication throughout?",
    ]
    for item in checklist:
        print(f"  {item}")
    print("=" * 70)


def show_optimal_solution():
    """Display the optimal solution"""
    print("\n" + "=" * 70)
    print("OPTIMAL SOLUTION:")
    print("=" * 70)
    print("""
from collections import Counter
from typing import List, Optional

def find_winner(votes: List[str]) -> Optional[str]:
    '''Find the candidate with the most votes.

    Time: O(n), Space: O(k) where k is unique candidates
    '''
    if not votes:
        return None

    vote_counts = Counter(votes)
    return vote_counts.most_common(1)[0][0]

# With tie detection:
def find_winner_with_ties(votes: List[str]) -> dict:
    if not votes:
        return {'winner': None, 'is_tie': False}

    vote_counts = Counter(votes)
    max_votes = max(vote_counts.values())
    winners = [c for c, v in vote_counts.items() if v == max_votes]

    return {
        'winner': winners[0] if len(winners) == 1 else winners,
        'vote_count': max_votes,
        'is_tie': len(winners) > 1,
        'all_results': dict(vote_counts)
    }
""")
    print("=" * 70)


def show_follow_ups():
    """Display common follow-up questions"""
    print("\n" + "=" * 70)
    print("COMMON FOLLOW-UP QUESTIONS:")
    print("=" * 70)
    questions = [
        "\n1. What if we have 1 billion votes?",
        "   → Discuss: Streaming, MapReduce, distributed systems",

        "\n2. What if votes come in real-time?",
        "   → Discuss: Incremental counting, event streams, Redis",

        "\n3. What if we need to prevent duplicate voting?",
        "   → Discuss: Voter IDs, authentication, fraud detection",

        "\n4. How would you scale this horizontally?",
        "   → Discuss: Partitioning, aggregation, coordination",

        "\n5. What if memory is limited?",
        "   → Discuss: External sorting, approximate algorithms, databases",

        "\n6. How would you monitor this in production?",
        "   → Discuss: Metrics, logging, alerting, observability",
    ]
    for q in questions:
        print(q)
    print("\n" + "=" * 70)


def run_test_cases():
    """Run through test cases"""
    print("\n" + "=" * 70)
    print("TEST CASES TO WALK THROUGH:")
    print("=" * 70)

    test_cases = [
        {
            'name': 'Example from problem',
            'input': ['c1', 'c2', 'c1', 'c2', 'c1', 'c2', 'c3', 'c4', 'c4'],
            'expected': 'c1 or c2 (both have 3 votes)'
        },
        {
            'name': 'Clear winner',
            'input': ['c1', 'c1', 'c1', 'c2', 'c2', 'c3'],
            'expected': 'c1 (3 votes)'
        },
        {
            'name': 'Empty list',
            'input': [],
            'expected': 'None'
        },
        {
            'name': 'Single vote',
            'input': ['c1'],
            'expected': 'c1'
        },
        {
            'name': 'Two-way tie',
            'input': ['c1', 'c1', 'c2', 'c2'],
            'expected': 'c1 and c2 (both have 2 votes)'
        },
        {
            'name': 'All same',
            'input': ['c1', 'c1', 'c1'],
            'expected': 'c1'
        }
    ]

    for i, tc in enumerate(test_cases, 1):
        print(f"\nTest {i}: {tc['name']}")
        print(f"  Input:    {tc['input']}")
        print(f"  Expected: {tc['expected']}")

    print("\n" + "=" * 70)


def main():
    """Main practice session"""
    print("\n🎯 ATLASSIAN VOTE COUNTER - PRACTICE SESSION\n")

    while True:
        print("\nOptions:")
        print("  1. Start timed practice (simulate interview)")
        print("  2. View optimal solution")
        print("  3. View test cases")
        print("  4. View follow-up questions")
        print("  5. View interview checklist")
        print("  6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == '1':
            start_time = practice_prompt()
            input("\n\nPress Enter when you've finished your solution...")
            elapsed = int(time.time() - start_time)
            minutes = elapsed // 60
            seconds = elapsed % 60
            print(f"\n⏱️  Time taken: {minutes}m {seconds}s")
            print("(Target: 15-20 minutes for coding)")
            show_checklist()

        elif choice == '2':
            show_optimal_solution()

        elif choice == '3':
            run_test_cases()

        elif choice == '4':
            show_follow_ups()

        elif choice == '5':
            show_checklist()

        elif choice == '6':
            print("\n👍 Good luck with your interview!")
            break

        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
