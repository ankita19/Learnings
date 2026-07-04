"""Support Agent Rating System - Atlassian Interview Question

Problem:
- Each support agent has an ID and receives ratings from 1-5
- Must support:
  1. Recording ratings
  2. Computing average rating
  3. Sorting by average rating
  4. Tie-breaking logic

Follow-up: Support weighted votes
"""

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import heapq
from enum import Enum


class TieBreakStrategy(Enum):
    """Different strategies for breaking ties in ratings"""
    AGENT_ID = "agent_id"  # Lower ID wins
    TOTAL_RATINGS = "total_ratings"  # More ratings wins
    RECENT_RATING = "recent_rating"  # Most recent rating wins
    HIGHEST_RATING = "highest_rating"  # Highest individual rating wins


@dataclass
class Agent:
    """Represents a support agent with ratings"""
    agent_id: str
    ratings: List[int] = field(default_factory=list)
    rating_timestamps: List[float] = field(default_factory=list)

    def add_rating(self, rating: int, timestamp: Optional[float] = None) -> None:
        """Add a rating for this agent (1-5)"""
        if not 1 <= rating <= 5:
            raise ValueError(f"Rating must be between 1-5, got {rating}")

        self.ratings.append(rating)
        if timestamp is not None:
            self.rating_timestamps.append(timestamp)

    def get_average_rating(self) -> float:
        """Calculate average rating"""
        if not self.ratings:
            return 0.0
        return sum(self.ratings) / len(self.ratings)

    def get_total_ratings(self) -> int:
        """Get total number of ratings"""
        return len(self.ratings)

    def get_highest_rating(self) -> int:
        """Get the highest individual rating"""
        return max(self.ratings) if self.ratings else 0

    def get_most_recent_rating(self) -> Optional[int]:
        """Get the most recent rating"""
        return self.ratings[-1] if self.ratings else None

    def __repr__(self) -> str:
        avg = self.get_average_rating()
        return f"Agent({self.agent_id}, avg={avg:.2f}, ratings={len(self.ratings)})"


class AgentRatingSystem:
    """Main system for managing agent ratings"""

    def __init__(self, tie_break_strategy: TieBreakStrategy = TieBreakStrategy.AGENT_ID):
        self.agents: Dict[str, Agent] = {}
        self.tie_break_strategy = tie_break_strategy

    def record_rating(self, agent_id: str, rating: int, timestamp: Optional[float] = None) -> None:
        """Record a rating for an agent

        Args:
            agent_id: Unique identifier for the agent
            rating: Rating value (1-5)
            timestamp: Optional timestamp for the rating
        """
        if agent_id not in self.agents:
            self.agents[agent_id] = Agent(agent_id)

        self.agents[agent_id].add_rating(rating, timestamp)

    def get_average_rating(self, agent_id: str) -> Optional[float]:
        """Get average rating for a specific agent"""
        if agent_id not in self.agents:
            return None
        return self.agents[agent_id].get_average_rating()

    def get_sorted_agents(self) -> List[Agent]:
        """Get all agents sorted by average rating (descending)

        In case of ties, uses the configured tie-break strategy.

        Returns:
            List of agents sorted by rating (highest first)
        """
        agents_list = list(self.agents.values())

        # Define sort key based on tie-break strategy
        def sort_key(agent: Agent) -> Tuple:
            avg_rating = agent.get_average_rating()

            if self.tie_break_strategy == TieBreakStrategy.AGENT_ID:
                # Higher avg first, then lower ID
                return (-avg_rating, agent.agent_id)

            elif self.tie_break_strategy == TieBreakStrategy.TOTAL_RATINGS:
                # Higher avg first, then more ratings
                return (-avg_rating, -agent.get_total_ratings(), agent.agent_id)

            elif self.tie_break_strategy == TieBreakStrategy.RECENT_RATING:
                # Higher avg first, then higher recent rating
                recent = agent.get_most_recent_rating() or 0
                return (-avg_rating, -recent, agent.agent_id)

            elif self.tie_break_strategy == TieBreakStrategy.HIGHEST_RATING:
                # Higher avg first, then higher max rating
                return (-avg_rating, -agent.get_highest_rating(), agent.agent_id)

            return (-avg_rating, agent.agent_id)

        return sorted(agents_list, key=sort_key)

    def get_top_k_agents(self, k: int) -> List[Agent]:
        """Get top K agents by rating (optimized with heap)

        Time: O(n log k) instead of O(n log n)
        """
        if k >= len(self.agents):
            return self.get_sorted_agents()

        # Use min heap of size k
        heap = []

        for agent in self.agents.values():
            avg_rating = agent.get_average_rating()
            # Use negative for max heap behavior
            item = (-avg_rating, agent.agent_id, agent)

            if len(heap) < k:
                heapq.heappush(heap, item)
            else:
                heapq.heappushpop(heap, item)

        # Extract and sort
        top_agents = [item[2] for item in heap]
        return sorted(top_agents,
                     key=lambda a: (-a.get_average_rating(), a.agent_id))

    def get_agent_rankings(self) -> Dict[str, int]:
        """Get ranking position for each agent (1-indexed)"""
        sorted_agents = self.get_sorted_agents()
        return {agent.agent_id: idx + 1
                for idx, agent in enumerate(sorted_agents)}

    def __repr__(self) -> str:
        return f"AgentRatingSystem(agents={len(self.agents)}, tie_break={self.tie_break_strategy.value})"


class WeightedAgentRatingSystem(AgentRatingSystem):
    """Extended system that supports weighted ratings

    Follow-up question: Add support for weighted votes

    Use cases for weights:
    - Recent ratings count more (time decay)
    - Enterprise customer ratings count more
    - Critical issue ratings count more
    """

    def __init__(self, tie_break_strategy: TieBreakStrategy = TieBreakStrategy.AGENT_ID):
        super().__init__(tie_break_strategy)
        self.rating_weights: Dict[str, List[float]] = defaultdict(list)

    def record_rating(self, agent_id: str, rating: int,
                     weight: float = 1.0,
                     timestamp: Optional[float] = None) -> None:
        """Record a weighted rating

        Args:
            agent_id: Unique identifier for the agent
            rating: Rating value (1-5)
            weight: Weight for this rating (default 1.0)
            timestamp: Optional timestamp
        """
        if weight < 0:
            raise ValueError(f"Weight must be non-negative, got {weight}")

        super().record_rating(agent_id, rating, timestamp)
        self.rating_weights[agent_id].append(weight)

    def get_average_rating(self, agent_id: str) -> Optional[float]:
        """Get weighted average rating for a specific agent"""
        if agent_id not in self.agents:
            return None

        agent = self.agents[agent_id]
        weights = self.rating_weights.get(agent_id, [])

        if not agent.ratings:
            return 0.0

        # If no weights recorded, fall back to simple average
        if not weights or len(weights) != len(agent.ratings):
            return agent.get_average_rating()

        # Weighted average: sum(rating * weight) / sum(weights)
        weighted_sum = sum(r * w for r, w in zip(agent.ratings, weights))
        total_weight = sum(weights)

        return weighted_sum / total_weight if total_weight > 0 else 0.0

    def get_sorted_agents(self) -> List[Agent]:
        """Get agents sorted by weighted average rating"""
        agents_list = list(self.agents.values())

        def sort_key(agent: Agent) -> Tuple:
            # Use weighted average
            avg_rating = self.get_average_rating(agent.agent_id) or 0

            if self.tie_break_strategy == TieBreakStrategy.AGENT_ID:
                return (-avg_rating, agent.agent_id)

            elif self.tie_break_strategy == TieBreakStrategy.TOTAL_RATINGS:
                return (-avg_rating, -agent.get_total_ratings(), agent.agent_id)

            return (-avg_rating, agent.agent_id)

        return sorted(agents_list, key=sort_key)


class TimeDecayWeightedSystem(WeightedAgentRatingSystem):
    """System with automatic time-decay weighting

    Recent ratings automatically count more than old ratings.
    Uses exponential decay: weight = e^(-λ * age_in_days)
    """

    def __init__(self, decay_rate: float = 0.1,
                 tie_break_strategy: TieBreakStrategy = TieBreakStrategy.AGENT_ID):
        """
        Args:
            decay_rate: Lambda parameter for exponential decay (higher = faster decay)
        """
        super().__init__(tie_break_strategy)
        self.decay_rate = decay_rate

    def calculate_time_weight(self, timestamp: float, current_time: float) -> float:
        """Calculate weight based on time decay"""
        import math
        age_days = (current_time - timestamp) / 86400  # Convert seconds to days
        return math.exp(-self.decay_rate * age_days)

    def get_average_rating(self, agent_id: str, current_time: Optional[float] = None) -> Optional[float]:
        """Get time-decay weighted average"""
        if agent_id not in self.agents:
            return None

        agent = self.agents[agent_id]

        if not agent.ratings:
            return 0.0

        if not agent.rating_timestamps:
            return agent.get_average_rating()

        # Use current time if not provided
        if current_time is None:
            import time
            current_time = time.time()

        # Calculate weights based on timestamps
        weights = [self.calculate_time_weight(ts, current_time)
                  for ts in agent.rating_timestamps]

        weighted_sum = sum(r * w for r, w in zip(agent.ratings, weights))
        total_weight = sum(weights)

        return weighted_sum / total_weight if total_weight > 0 else 0.0


# Example usage and demonstrations
def demo_basic_system():
    """Demonstrate basic rating system"""
    print("=" * 70)
    print("BASIC AGENT RATING SYSTEM")
    print("=" * 70)

    system = AgentRatingSystem(TieBreakStrategy.AGENT_ID)

    # Record some ratings
    system.record_rating("agent_001", 5)
    system.record_rating("agent_001", 4)
    system.record_rating("agent_001", 5)

    system.record_rating("agent_002", 5)
    system.record_rating("agent_002", 5)
    system.record_rating("agent_002", 4)

    system.record_rating("agent_003", 3)
    system.record_rating("agent_003", 4)

    # Get averages
    print("\nAverage Ratings:")
    for agent_id in ["agent_001", "agent_002", "agent_003"]:
        avg = system.get_average_rating(agent_id)
        print(f"  {agent_id}: {avg:.2f}")

    # Get sorted list
    print("\nSorted Agents (highest to lowest):")
    for idx, agent in enumerate(system.get_sorted_agents(), 1):
        print(f"  {idx}. {agent}")

    # Get rankings
    print("\nAgent Rankings:")
    rankings = system.get_agent_rankings()
    for agent_id, rank in sorted(rankings.items()):
        print(f"  {agent_id}: Rank #{rank}")


def demo_tie_breaking():
    """Demonstrate different tie-breaking strategies"""
    print("\n" + "=" * 70)
    print("TIE-BREAKING STRATEGIES")
    print("=" * 70)

    # Create scenario with ties
    data = [
        ("agent_001", [5, 5, 4]),  # avg = 4.67, 3 ratings
        ("agent_002", [5, 5, 4]),  # avg = 4.67, 3 ratings
        ("agent_003", [5, 4]),     # avg = 4.50, 2 ratings
    ]

    strategies = [
        TieBreakStrategy.AGENT_ID,
        TieBreakStrategy.TOTAL_RATINGS,
    ]

    for strategy in strategies:
        print(f"\nStrategy: {strategy.value}")
        system = AgentRatingSystem(strategy)

        for agent_id, ratings in data:
            for rating in ratings:
                system.record_rating(agent_id, rating)

        for idx, agent in enumerate(system.get_sorted_agents(), 1):
            print(f"  {idx}. {agent}")


def demo_weighted_system():
    """Demonstrate weighted rating system"""
    print("\n" + "=" * 70)
    print("WEIGHTED RATING SYSTEM")
    print("=" * 70)

    system = WeightedAgentRatingSystem()

    # agent_001: regular customer ratings
    system.record_rating("agent_001", 5, weight=1.0)
    system.record_rating("agent_001", 4, weight=1.0)
    system.record_rating("agent_001", 5, weight=1.0)

    # agent_002: mix of regular and enterprise (2x weight)
    system.record_rating("agent_002", 4, weight=1.0)
    system.record_rating("agent_002", 5, weight=2.0)  # Enterprise customer
    system.record_rating("agent_002", 4, weight=1.0)

    print("\nWeighted Averages:")
    print(f"  agent_001: {system.get_average_rating('agent_001'):.2f}")
    print(f"  agent_002: {system.get_average_rating('agent_002'):.2f}")

    print("\nSorted:")
    for idx, agent in enumerate(system.get_sorted_agents(), 1):
        avg = system.get_average_rating(agent.agent_id)
        print(f"  {idx}. {agent.agent_id}: {avg:.2f}")


if __name__ == "__main__":
    demo_basic_system()
    demo_tie_breaking()
    demo_weighted_system()
