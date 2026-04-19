from typing import Dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ⏱️ Time Complexity: O(n) - single pass over strings
        # 💾 Space Complexity: O(1) - max 26 lowercase letters in map
        # 📌 Pattern: Frequency Hash Map
        # 🔑 Key Insight: Anagrams have identical character counts
        
        if len(s) != len(t):
            return False
            
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False