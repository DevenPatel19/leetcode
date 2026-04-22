class Solution:
    # Method taking two strings, returns a boolean
    def isAnagram(self, s: str, t: str) -> bool:                              # O(1)

        # If strings differ in length, they can't be anagrams — exit early
        if len(s) != len(t):                                                  # O(1)
            # Short-circuit exit — no need to check further
            return False                                                       # O(1)

        # Empty dict to store character frequencies from string s
        count = {}                                                             # O(1)
# Create a reference of first word
        # Loop through every character in s
        for char in s:                                                         # O(n)
            # If char exists, increment its count; if not, start at 0 then add 1
            count[char] = count.get(char, 0) + 1                              # O(1)
# Compare entire string "-" letter counts from the reference until something isn't available
        # Loop through every character in t
        for char in t:                                                         # O(n)
            # If char never appeared in s, OR we've used up all its occurrences
            if char not in count or count[char] == 0:                         # O(1)
                # t has a char that s doesn't (or has more of) → not an anagram
                return False                                                   # O(1)
            # Cancel out one occurrence of this char from s's frequency map
            count[char] -= 1                                                   # O(1)
# All Tests Passed then return True
        # All characters matched perfectly — it's an anagram
        return True                                                            # O(1)


# Only runs this block if script is executed directly (not imported)
if __name__ == "__main__":                                                     # O(1)
    # Create an instance of the Solution class
    sol = Solution()                                                           # O(1)
    # Same letters rearranged → True
    print(sol.isAnagram("anagram", "nagaram"))                                # O(n)
    # 'c' not in "rat" → False
    print(sol.isAnagram("rat", "car"))                                        # O(n)