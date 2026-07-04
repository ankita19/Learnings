"""Unit tests for Agent Rating System"""

import pytest
import time
from agent_rating_system import (
    Agent,
    AgentRatingSystem,
    WeightedAgentRatingSystem,
    TimeDecayWeightedSystem,
    TieBreakStrategy
)


class TestAgent:
    """Test Agent class functionality"""

    def test_add_rating_valid(self):
        agent = Agent("agent_001")
        agent.add_rating(5)
        assert len(agent.ratings) == 1
        assert agent.ratings[0] == 5

    def test_add_rating_invalid(self):
        agent = Agent("agent_001")
        with pytest.raises(ValueError):
            agent.add_rating(6)  # Out of range

        with pytest.raises(ValueError):
            agent.add_rating(0)  # Out of range

    def test_average_rating(self):
        agent = Agent("agent_001")
        agent.add_rating(5)
        agent.add_rating(3)
        agent.add_rating(4)
        assert agent.get_average_rating() == 4.0

    def test_average_rating_empty(self):
        agent = Agent("agent_001")
        assert agent.get_average_rating() == 0.0

    def test_total_ratings(self):
        agent = Agent("agent_001")
        agent.add_rating(5)
        agent.add_rating(4)
        assert agent.get_total_ratings() == 2

    def test_highest_rating(self):
        agent = Agent("agent_001")
        agent.add_rating(3)
        agent.add_rating(5)
        agent.add_rating(2)
        assert agent.get_highest_rating() == 5

    def test_most_recent_rating(self):
        agent = Agent("agent_001")
        agent.add_rating(3)
        agent.add_rating(5)
        agent.add_rating(2)
        assert agent.get_most_recent_rating() == 2


class TestAgentRatingSystem:
    """Test basic rating system"""

    def test_record_rating_new_agent(self):
        system = AgentRatingSystem()
        system.record_rating("agent_001", 5)
        assert "agent_001" in system.agents
        assert len(system.agents["agent_001"].ratings) == 1

    def test_record_rating_existing_agent(self):
        system = AgentRatingSystem()
        system.record_rating("agent_001", 5)
        system.record_rating("agent_001", 4)
        assert len(system.agents["agent_001"].ratings) == 2

    def test_get_average_rating(self):
        system = AgentRatingSystem()
        system.record_rating("agent_001", 5)
        system.record_rating("agent_001", 3)
        avg = system.get_average_rating("agent_001")
        assert avg == 4.0

    def test_get_average_rating_nonexistent(self):
        system = AgentRatingSystem()
        assert system.get_average_rating("agent_999") is None

    def test_sorted_agents_basic(self):
        system = AgentRatingSystem()

        system.record_rating("agent_001", 5)
        system.record_rating("agent_001", 5)  # avg = 5.0

        system.record_rating("agent_002", 4)
        system.record_rating("agent_002", 4)  # avg = 4.0

        system.record_rating("agent_003", 3)  # avg = 3.0

        sorted_agents = system.get_sorted_agents()

        assert sorted_agents[0].agent_id == "agent_001"
        assert sorted_agents[1].agent_id == "agent_002"
        assert sorted_agents[2].agent_id == "agent_003"

    def test_get_agent_rankings(self):
        system = AgentRatingSystem()

        system.record_rating("agent_001", 5)
        system.record_rating("agent_002", 4)
        system.record_rating("agent_003", 3)

        rankings = system.get_agent_rankings()

        assert rankings["agent_001"] == 1
        assert rankings["agent_002"] == 2
        assert rankings["agent_003"] == 3


class TestTieBreaking:
    """Test different tie-breaking strategies"""

    def test_tie_break_by_agent_id(self):
        system = AgentRatingSystem(TieBreakStrategy.AGENT_ID)

        # Both have same average
        system.record_rating("agent_002", 4)
        system.record_rating("agent_001", 4)

        sorted_agents = system.get_sorted_agents()

        # Lower ID should come first
        assert sorted_agents[0].agent_id == "agent_001"
        assert sorted_agents[1].agent_id == "agent_002"

    def test_tie_break_by_total_ratings(self):
        system = AgentRatingSystem(TieBreakStrategy.TOTAL_RATINGS)

        # Same average, different total ratings
        system.record_rating("agent_001", 4)
        system.record_rating("agent_001", 4)  # 2 ratings

        system.record_rating("agent_002", 4)  # 1 rating

        sorted_agents = system.get_sorted_agents()

        # More ratings should come first
        assert sorted_agents[0].agent_id == "agent_001"
        assert sorted_agents[1].agent_id == "agent_002"

    def test_tie_break_by_highest_rating(self):
        system = AgentRatingSystem(TieBreakStrategy.HIGHEST_RATING)

        # Same average, different max
        system.record_rating("agent_001", 5)
        system.record_rating("agent_001", 3)  # avg=4, max=5

        system.record_rating("agent_002", 4)
        system.record_rating("agent_002", 4)  # avg=4, max=4

        sorted_agents = system.get_sorted_agents()

        # Higher max rating should come first
        assert sorted_agents[0].agent_id == "agent_001"


class TestTopKAgents:
    """Test top-K functionality"""

    def test_top_k_less_than_total(self):
        system = AgentRatingSystem()

        for i in range(10):
            system.record_rating(f"agent_{i:03d}", 5 - i % 5)

        top_3 = system.get_top_k_agents(3)
        assert len(top_3) == 3

    def test_top_k_more_than_total(self):
        system = AgentRatingSystem()

        system.record_rating("agent_001", 5)
        system.record_rating("agent_002", 4)

        top_5 = system.get_top_k_agents(5)
        assert len(top_5) == 2


class TestWeightedRatingSystem:
    """Test weighted rating system"""

    def test_weighted_average(self):
        system = WeightedAgentRatingSystem()

        # Rating 5 with weight 2, rating 3 with weight 1
        # Weighted avg = (5*2 + 3*1) / (2+1) = 13/3 = 4.33
        system.record_rating("agent_001", 5, weight=2.0)
        system.record_rating("agent_001", 3, weight=1.0)

        avg = system.get_average_rating("agent_001")
        assert abs(avg - 4.333) < 0.01

    def test_weighted_vs_unweighted(self):
        weighted_system = WeightedAgentRatingSystem()
        unweighted_system = AgentRatingSystem()

        # Same ratings, different weights
        ratings = [5, 3, 4]

        for r in ratings:
            unweighted_system.record_rating("agent_001", r)

        weighted_system.record_rating("agent_001", 5, weight=3.0)
        weighted_system.record_rating("agent_001", 3, weight=1.0)
        weighted_system.record_rating("agent_001", 4, weight=1.0)

        unweighted_avg = unweighted_system.get_average_rating("agent_001")
        weighted_avg = weighted_system.get_average_rating("agent_001")

        # Weighted should be higher (5 has more weight)
        assert weighted_avg > unweighted_avg

    def test_zero_weight(self):
        system = WeightedAgentRatingSystem()
        system.record_rating("agent_001", 5, weight=1.0)
        system.record_rating("agent_001", 1, weight=0.0)  # Should not affect

        avg = system.get_average_rating("agent_001")
        assert avg == 5.0

    def test_negative_weight_raises(self):
        system = WeightedAgentRatingSystem()
        with pytest.raises(ValueError):
            system.record_rating("agent_001", 5, weight=-1.0)


class TestTimeDecaySystem:
    """Test time-decay weighted system"""

    def test_recent_ratings_count_more(self):
        system = TimeDecayWeightedSystem(decay_rate=0.1)

        current_time = time.time()
        old_time = current_time - 30 * 86400  # 30 days ago

        # Old rating: 5, recent rating: 3
        system.record_rating("agent_001", 5, timestamp=old_time)
        system.record_rating("agent_001", 3, timestamp=current_time)

        avg = system.get_average_rating("agent_001", current_time=current_time)

        # Average should be closer to 3 (recent) than to 4 (simple avg)
        simple_avg = 4.0
        assert avg < simple_avg


class TestEdgeCases:
    """Test edge cases and error conditions"""

    def test_empty_system(self):
        system = AgentRatingSystem()
        assert len(system.get_sorted_agents()) == 0

    def test_single_agent(self):
        system = AgentRatingSystem()
        system.record_rating("agent_001", 5)

        sorted_agents = system.get_sorted_agents()
        assert len(sorted_agents) == 1
        assert sorted_agents[0].agent_id == "agent_001"

    def test_all_same_rating(self):
        system = AgentRatingSystem()
        system.record_rating("agent_001", 4)
        system.record_rating("agent_002", 4)
        system.record_rating("agent_003", 4)

        sorted_agents = system.get_sorted_agents()
        # All should have same average, sorted by ID
        assert sorted_agents[0].agent_id == "agent_001"


class TestScalability:
    """Test with larger datasets"""

    def test_many_agents(self):
        system = AgentRatingSystem()

        # Create 1000 agents with random ratings
        for i in range(1000):
            for _ in range(5):
                rating = (i % 5) + 1
                system.record_rating(f"agent_{i:04d}", rating)

        sorted_agents = system.get_sorted_agents()
        assert len(sorted_agents) == 1000

    def test_many_ratings_per_agent(self):
        system = AgentRatingSystem()

        # Single agent with 10000 ratings
        for i in range(10000):
            system.record_rating("agent_001", (i % 5) + 1)

        avg = system.get_average_rating("agent_001")
        assert avg is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
