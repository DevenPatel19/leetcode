from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ⏱️ Time Complexity: O(n) - single pass lookup
        # 💾 Space Complexity: O(n) - hash map stores up to n indices
        # 📌 Pattern: Hash Map Complement
        # 🔑 Key Insight: Store complement BEFORE checking current number
        

        # ✅ WRITE YOUR LOGIC BELOW THIS LINE
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
        # ✅ WRITE YOUR LOGIC ABOVE THIS LINE
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))   # [0, 1]
    print(sol.twoSum([3,2,4], 6))       # [1, 2]
    print(sol.twoSum([3,3], 6))         # [0, 1]
    
    
    """ 
    Solution from: April 22 2026 -
           seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return[]
    """