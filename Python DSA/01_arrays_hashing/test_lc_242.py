import pytest
from lc_242_valid_anagram_v1 import Solution

def test_isAnagram_happy_path():
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") == True
    assert sol.isAnagram("rat", "car") == False

def test_isAnagram_edge_cases():
    sol = Solution()
    assert sol.isAnagram("a", "a") == True           # Single char
    assert sol.isAnagram("ab", "abc") == False       # Length mismatch
    assert sol.isAnagram("aa", "a") == False         # Same prefix, diff length
    assert sol.isAnagram("code", "doce") == True     # Mixed order