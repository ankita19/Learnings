
import pytest

from src.reverse_words import reverse_words, reverse_words_preserve_spaces_regex


def test_reverse_words_examples():
	f = reverse_words
	assert f("") == ""
	assert f("   ") == "   "
	assert f("hello") == "hello"
	assert f("hello world") == "olleh dlrow"
	assert f("  hello  world ") == "  olleh  dlrow "
	assert f("a b c") == "a b c"
	
def test_reverse_words_alternative_examples():
    f = reverse_words_preserve_spaces_regex
    assert f("") == ""
    assert f("   ") == "   "
    assert f("hello") == "hello"
    assert f("hello world") == "olleh dlrow"
    assert f("  hello  world ") == "  olleh  dlrow "
    assert f("a b c") == "a b c"