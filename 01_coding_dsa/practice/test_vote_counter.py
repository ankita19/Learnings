"""Unit tests for vote counter - demonstrate testing mindset for Principal role"""

import pytest
from vote_counter import (
    find_winner_basic,
    find_winner_with_tie_detection,
    find_winner_manual,
    find_winner_streaming,
    find_top_k_candidates,
    find_winner_robust
)


class TestBasicFunctionality:
    """Test basic winner finding functionality"""

    def test_clear_winner(self):
        votes = ['c1', 'c2', 'c1', 'c2', 'c1', 'c2', 'c3', 'c4', 'c4']
        # c1 and c2 both have 3 votes, but c1 appears first
        result = find_winner_basic(votes)
        assert result in ['c1', 'c2']

    def test_single_vote(self):
        votes = ['c1']
        assert find_winner_basic(votes) == 'c1'

    def test_all_same_candidate(self):
        votes = ['c1', 'c1', 'c1', 'c1']
        assert find_winner_basic(votes) == 'c1'

    def test_two_candidates(self):
        votes = ['c1', 'c2', 'c1']
        assert find_winner_basic(votes) == 'c1'


class TestEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_empty_votes(self):
        assert find_winner_basic([]) is None

    def test_tie_scenario(self):
        votes = ['c1', 'c1', 'c2', 'c2']
        result = find_winner_with_tie_detection(votes)
        assert result['is_tie'] is True
        assert result['vote_count'] == 2
        assert set(result['winner']) == {'c1', 'c2'}

    def test_three_way_tie(self):
        votes = ['c1', 'c2', 'c3']
        result = find_winner_with_tie_detection(votes)
        assert result['is_tie'] is True
        assert len(result['winner']) == 3


class TestRobustImplementation:
    """Test production-grade error handling"""

    def test_none_input(self):
        with pytest.raises(ValueError):
            find_winner_robust(None)

    def test_invalid_type(self):
        with pytest.raises(TypeError):
            find_winner_robust("not a list")

    def test_with_invalid_votes(self):
        votes = ['c1', None, 'c2', '', 'c1']
        result = find_winner_robust(votes)
        assert result['winner'] == 'c1'
        assert result['vote_count'] == 2
        assert result['invalid_votes'] == 2

    def test_all_invalid_votes(self):
        votes = [None, '', None]
        result = find_winner_robust(votes)
        assert result['winner'] is None
        assert result['invalid_votes'] == 3


class TestTopKCandidates:
    """Test top K candidates functionality"""

    def test_top_3(self):
        votes = ['c1', 'c1', 'c1', 'c2', 'c2', 'c3', 'c4']
        result = find_top_k_candidates(votes, k=3)
        assert len(result) == 3
        assert result[0] == ('c1', 3)
        assert result[1] == ('c2', 2)

    def test_k_greater_than_candidates(self):
        votes = ['c1', 'c2']
        result = find_top_k_candidates(votes, k=5)
        assert len(result) == 2


class TestConsistencyAcrossImplementations:
    """Ensure all implementations produce consistent results"""

    def test_all_implementations_match(self):
        votes = ['c1', 'c2', 'c1', 'c3', 'c1', 'c2']

        basic = find_winner_basic(votes)
        manual = find_winner_manual(votes)
        streaming = find_winner_streaming(votes)
        detailed = find_winner_with_tie_detection(votes)

        assert basic == manual == streaming
        assert basic == detailed['winner']


class TestPerformance:
    """Test with larger datasets"""

    def test_large_dataset(self):
        # 1 million votes
        votes = ['c1'] * 400000 + ['c2'] * 300000 + ['c3'] * 300000
        result = find_winner_basic(votes)
        assert result == 'c1'

    def test_many_candidates(self):
        # 10000 unique candidates
        votes = [f'c{i}' for i in range(10000)]
        result = find_winner_basic(votes)
        assert result is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
