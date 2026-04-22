from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # ⏱️ Time Complexity: O(n) - single pass through array
        # 💾 Space Complexity: O(n) - set stores up to n unique elements
        # 📌 Pattern: Hash Set Lookup
        # 🔑 Key Insight: Track seen elements, return True on first repeat

        # Initialize an empty hash set to track visited numbers
        seen = set()                                                       # O(1)

        # Iterate through each element in the input array
        for num in nums:                                                   # O(n)
            # Check if current element was already encountered
            if num in seen:                                                # O(1)
                # Duplicate detected, exit early with positive result
                return True                                                # O(1)
            # Record current element for future lookups
            seen.add(num)                                                  # O(1)

        # Entire array processed without finding duplicates
        return False                                                       # O(1)

        # ✅ WRITE YOUR LOGIC BELOW THIS LINE
        pass
        # ✅ WRITE YOUR LOGIC ABOVE THIS LINE

# --- AUTOMATED TEST RUNNER (DO NOT MODIFY) ---
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([1], False),
        ([-5, -2, -5], True),
    ]
    passed = 0
    for test in tests:
        inputs, expected = test[:-1], test[-1]
        result = sol.containsDuplicate(*inputs)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result == expected: passed += 1
        print(f"{status} | containsDuplicate({inputs}) → {result} (expected {expected})")
    print(f"\n📊 Results: {passed}/{len(tests)} passed")

# =============================================================================
# 📜 HISTORY & ATTEMPTS (Comment out after each session)
# =============================================================================
# PASTE PREVIOUS REVIEW BLOCKS HERE