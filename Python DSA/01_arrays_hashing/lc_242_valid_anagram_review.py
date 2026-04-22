from typing import Dict
"""_summary_
# TYPE = TEMPLATE
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ⏱️ Time: O(n) | 💾 Space: O(1)
        # 📌 Pattern: Frequency Hash Map
        # 🔑 Key Insight: Count chars in s, subtract using t, verify all zero
        
        # ✅ WRITE YOUR LOGIC BELOW THIS LINE
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
        # ✅ WRITE YOUR LOGIC ABOVE THIS LINE

# --- AUTOMATED TEST RUNNER (DO NOT MODIFY) ---
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
        ("ab", "ba", True),
        ("", "", True),
        ("aa", "aaa", False),
    ]
    passed = 0
    for s, t, expected in tests:
        result = sol.isAnagram(s, t)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result == expected: passed += 1
        print(f"{status} | isAnagram('{s}', '{t}') → {result} (expected {expected})")
    print(f"\n📊 Results: {passed}/{len(tests)} passed")

      # TYPE : TEMPLATE
"""

# April 22 2026
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ⏱️ Time: O(n) | 💾 Space: O(1)
        # 📌 Pattern: Frequency Hash Map
        # 🔑 Key Insight: Count chars in s, subtract using t, verify all zero
        
        # ✅ WRITE YOUR LOGIC BELOW THIS LINE
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
        # ✅ WRITE YOUR LOGIC ABOVE THIS LINE

# --- AUTOMATED TEST RUNNER (DO NOT MODIFY) ---
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
        ("ab", "ba", True),
        ("", "", True),
        ("aa", "aaa", False),
    ]
    passed = 0
    for s, t, expected in tests:
        result = sol.isAnagram(s, t)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result == expected: passed += 1
        print(f"{status} | isAnagram('{s}', '{t}') → {result} (expected {expected})")
    print(f"\n📊 Results: {passed}/{len(tests)} passed")

# APRIL 20, 2026
# from typing import Dict

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # ⏱️ Time: O(n) | 💾 Space: O(1)
#         # 📌 Pattern: Frequency Hash Map
#         # 🔑 Key Insight: Count chars in s, subtract using t, verify all zero
        
#         # ✅ WRITE YOUR LOGIC BELOW THIS LINE
#         if len(s) != len(t):
#             return False
            
#         count = {}
#         for char in s:
#             count[char] = count.get(char, 0) + 1
#         for char in t:
#             if char not in count or count[char] == 0:
#                 return False
#             count[char] -= 1
#         return True
#         # ✅ WRITE YOUR LOGIC ABOVE THIS LINE

# # --- AUTOMATED TEST RUNNER (DO NOT MODIFY) ---
# if __name__ == "__main__":
#     sol = Solution()
#     tests = [
#         ("anagram", "nagaram", True),
#         ("rat", "car", False),
#         ("a", "ab", False),
#         ("ab", "ba", True),
#         ("", "", True),
#         ("aa", "aaa", False),
#     ]
#     passed = 0
#     for s, t, expected in tests:
#         result = sol.isAnagram(s, t)
#         status = "✅ PASS" if result == expected else "❌ FAIL"
#         if result == expected: passed += 1
#         print(f"{status} | isAnagram('{s}', '{t}') → {result} (expected {expected})")
#     print(f"\n📊 Results: {passed}/{len(tests)} passed")