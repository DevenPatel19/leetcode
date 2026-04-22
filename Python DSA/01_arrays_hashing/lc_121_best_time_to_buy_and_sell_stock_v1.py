from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ⏱️ Time Complexity: O(n) - single pass
        # 💾 Space Complexity: O(1) - two variables only
        # 📌 Pattern: Single-Pass Min Tracking (Greedy)
        # 🔑 Key Insight: Track lowest price seen so far, update max profit at each step

        # ✅ WRITE YOUR LOGIC BELOW THIS LINE
        pass
        # ✅ WRITE YOUR LOGIC ABOVE THIS LINE

# --- AUTOMATED TEST RUNNER (DO NOT MODIFY) ---
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1, 2], 1),
        ([2, 1, 4], 3),
        ([1], 0),
    ]
    passed = 0
    for prices, expected in tests:
        result = sol.maxProfit(prices)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result == expected: passed += 1
        print(f"{status} | maxProfit({prices}) → {result} (expected {expected})")
    print(f"\n📊 Results: {passed}/{len(tests)} passed")