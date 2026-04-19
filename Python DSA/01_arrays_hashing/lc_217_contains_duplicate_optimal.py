from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # ‚è±Ô∏è Time Complexity: O(n) - single pass
        # Ì≤æ Space Complexity: O(n) - hash set storage
        # Ì≥å Pattern: Hash Set Lookup
        # Ì¥ë Key Insight: Check existence BEFORE adding to set
        
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.containsDuplicate([1,2,3,1]))
    print("Test 2:", sol.containsDuplicate([1,2,3,4]))
