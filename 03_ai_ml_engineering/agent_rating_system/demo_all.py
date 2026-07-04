"""
Demo script for both Atlassian interview problems
Run this to see both implementations in action
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from vote_counter import (
    find_winner_basic,
    find_winner_with_tie_detection,
    find_top_k_candidates
)
from agent_rating_system import (
    AgentRatingSystem,
    WeightedAgentRatingSystem,
    TieBreakStrategy
)


def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def demo_vote_counter():
    """Demonstrate vote counter problem"""
    print_header("PROBLEM 1: VOTE COUNTER")

    # Test case from problem
    votes = ['c1', 'c2', 'c1', 'c2', 'c1', 'c2', 'c3', 'c4', 'c4']

    print("\nInput votes:")
    print(f"  {votes}")

    # Basic winner
    winner = find_winner_basic(votes)
    print(f"\nBasic winner: {winner}")

    # Detailed result with tie detection
    result = find_winner_with_tie_detection(votes)
    print(f"\nDetailed result:")
    print(f"  Winner: {result['winner']}")
    print(f"  Vote count: {result['vote_count']}")
    print(f"  Is tie: {result['is_tie']}")
    print(f"  All results: {result['all_results']}")

    # Top K candidates
    top_3 = find_top_k_candidates(votes, k=3)
    print(f"\nTop 3 candidates:")
    for i, (candidate, count) in enumerate(top_3, 1):
        print(f"  {i}. {candidate}: {count} votes")

    # Edge cases
    print("\n" + "-" * 70)
    print("Edge Cases:")
    print(f"  Empty list: {find_winner_basic([])}")
    print(f"  Single vote: {find_winner_basic(['c1'])}")
    print(f"  All same: {find_winner_basic(['c1', 'c1', 'c1'])}")

    # Tie scenario
    tie_votes = ['c1', 'c1', 'c2', 'c2']
    tie_result = find_winner_with_tie_detection(tie_votes)
    print(f"\n  Tie scenario {tie_votes}:")
    print(f"    Winners: {tie_result['winner']}")
    print(f"    Is tie: {tie_result['is_tie']}")


def demo_agent_rating_system():
    """Demonstrate agent rating system"""
    print_header("PROBLEM 2: AGENT RATING SYSTEM")

    # Basic system
    print("\n" + "-" * 70)
    print("Basic System (Tie-break by Agent ID)")
    print("-" * 70)

    system = AgentRatingSystem(TieBreakStrategy.AGENT_ID)

    # Add ratings
    print("\nAdding ratings...")
    ratings_data = [
        ("agent_alice", [5, 5, 4]),    # avg = 4.67
        ("agent_bob", [5, 4, 5]),      # avg = 4.67 (same as Alice)
        ("agent_charlie", [4, 4, 4]),  # avg = 4.00
        ("agent_diana", [5, 5, 5]),    # avg = 5.00
    ]

    for agent_id, ratings in ratings_data:
        for rating in ratings:
            system.record_rating(agent_id, rating)
        avg = system.get_average_rating(agent_id)
        print(f"  {agent_id}: {ratings} → avg = {avg:.2f}")

    # Get sorted agents
    print("\nSorted agents (highest to lowest):")
    for i, agent in enumerate(system.get_sorted_agents(), 1):
        avg = system.get_average_rating(agent.agent_id)
        print(f"  {i}. {agent.agent_id}: {avg:.2f} ({agent.get_total_ratings()} ratings)")

    # Show tie-breaking in action
    print("\nNote: Alice and Bob both have 4.67 avg, but Alice comes first")
    print("      due to tie-breaking by agent_id (alphabetical)")

    # Rankings
    print("\nAgent Rankings:")
    rankings = system.get_agent_rankings()
    for agent_id in sorted(rankings.keys()):
        print(f"  {agent_id}: Rank #{rankings[agent_id]}")


def demo_tie_breaking_strategies():
    """Demonstrate different tie-breaking strategies"""
    print_header("TIE-BREAKING STRATEGIES")

    # Same data for all systems
    data = [
        ("agent_001", [5, 5, 4]),      # avg = 4.67, 3 ratings
        ("agent_002", [5, 5, 4, 4]),   # avg = 4.50, 4 ratings
        ("agent_003", [5, 5, 4]),      # avg = 4.67, 3 ratings (tie with 001)
    ]

    strategies = [
        TieBreakStrategy.AGENT_ID,
        TieBreakStrategy.TOTAL_RATINGS,
    ]

    for strategy in strategies:
        print(f"\n{'-' * 70}")
        print(f"Strategy: {strategy.value}")
        print("-" * 70)

        system = AgentRatingSystem(strategy)

        for agent_id, ratings in data:
            for rating in ratings:
                system.record_rating(agent_id, rating)

        for i, agent in enumerate(system.get_sorted_agents(), 1):
            avg = agent.get_average_rating()
            total = agent.get_total_ratings()
            print(f"  {i}. {agent.agent_id}: avg={avg:.2f}, ratings={total}")


def demo_weighted_system():
    """Demonstrate weighted rating system"""
    print_header("WEIGHTED RATING SYSTEM (Follow-up)")

    print("\n" + "-" * 70)
    print("Scenario: Enterprise customer ratings count 2x more")
    print("-" * 70)

    system = WeightedAgentRatingSystem()

    # Agent 1: All regular customers
    print("\nAgent Alice - All regular customers:")
    system.record_rating("agent_alice", 5, weight=1.0)
    system.record_rating("agent_alice", 4, weight=1.0)
    system.record_rating("agent_alice", 5, weight=1.0)
    print("  Ratings: [5 (w=1.0), 4 (w=1.0), 5 (w=1.0)]")
    print("  Simple average: 4.67")
    print(f"  Weighted average: {system.get_average_rating('agent_alice'):.2f}")

    # Agent 2: Mix of regular and enterprise
    print("\nAgent Bob - Mix of regular and enterprise customers:")
    system.record_rating("agent_bob", 4, weight=1.0)
    system.record_rating("agent_bob", 5, weight=2.0)  # Enterprise
    system.record_rating("agent_bob", 4, weight=1.0)
    print("  Ratings: [4 (w=1.0), 5 (w=2.0), 4 (w=1.0)]")
    print("  Simple average: 4.33")
    weighted_avg = system.get_average_rating('agent_bob')
    print(f"  Weighted average: {weighted_avg:.2f}")
    print("  Calculation: (4*1 + 5*2 + 4*1) / (1+2+1) = 18/4 = 4.50")

    # Show sorted results
    print("\n" + "-" * 70)
    print("Sorted by weighted average:")
    print("-" * 70)
    for i, agent in enumerate(system.get_sorted_agents(), 1):
        avg = system.get_average_rating(agent.agent_id)
        print(f"  {i}. {agent.agent_id}: {avg:.2f}")


def demo_edge_cases():
    """Demonstrate edge case handling"""
    print_header("EDGE CASES & ERROR HANDLING")

    system = AgentRatingSystem()

    # Test 1: Empty system
    print("\nTest 1: Query non-existent agent")
    result = system.get_average_rating("nonexistent_agent")
    print(f"  Result: {result}")

    # Test 2: Invalid rating
    print("\nTest 2: Invalid rating value")
    try:
        system.record_rating("agent_001", 6)  # Out of range
        print("  ❌ Should have raised ValueError!")
    except ValueError as e:
        print(f"  ✓ Correctly raised ValueError: {e}")

    # Test 3: Empty ratings list
    print("\nTest 3: Empty sorted list")
    empty_system = AgentRatingSystem()
    sorted_agents = empty_system.get_sorted_agents()
    print(f"  Result: {sorted_agents} (length: {len(sorted_agents)})")

    # Test 4: Agent with no ratings
    print("\nTest 4: Agent gets first rating")
    system.record_rating("new_agent", 5)
    avg = system.get_average_rating("new_agent")
    print(f"  First rating: 5")
    print(f"  Average: {avg}")


def main_menu():
    """Interactive menu for demos"""
    while True:
        print("\n" + "=" * 70)
        print(" ATLASSIAN INTERVIEW PROBLEMS - DEMO")
        print("=" * 70)
        print("\nChoose a demo:")
        print("  1. Vote Counter (Problem 1)")
        print("  2. Agent Rating System - Basic (Problem 2)")
        print("  3. Agent Rating System - Tie-breaking Strategies")
        print("  4. Agent Rating System - Weighted Ratings (Follow-up)")
        print("  5. Edge Cases & Error Handling")
        print("  6. Run All Demos")
        print("  7. Exit")

        choice = input("\nEnter choice (1-7): ").strip()

        if choice == '1':
            demo_vote_counter()
        elif choice == '2':
            demo_agent_rating_system()
        elif choice == '3':
            demo_tie_breaking_strategies()
        elif choice == '4':
            demo_weighted_system()
        elif choice == '5':
            demo_edge_cases()
        elif choice == '6':
            demo_vote_counter()
            demo_agent_rating_system()
            demo_tie_breaking_strategies()
            demo_weighted_system()
            demo_edge_cases()
            print("\n" + "=" * 70)
            print(" ALL DEMOS COMPLETED")
            print("=" * 70)
        elif choice == '7':
            print("\n👍 Good luck with your interview!")
            break
        else:
            print("\n❌ Invalid choice. Please enter 1-7.")

        if choice in ['1', '2', '3', '4', '5', '6']:
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    # Check if running in interactive mode
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        # Run all demos non-interactively
        demo_vote_counter()
        demo_agent_rating_system()
        demo_tie_breaking_strategies()
        demo_weighted_system()
        demo_edge_cases()
    else:
        # Interactive menu
        main_menu()
