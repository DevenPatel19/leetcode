from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ⏱️ Time Complexity: O(n) - single pass lookup
        # 💾 Space Complexity: O(n) - hash map stores up to n indices
        # 📌 Pattern: Hash Map Complement
        # 🔑 Key Insight: Store complement BEFORE checking current number
        
         # Initialize an empty hash map to store number -> index mappings
        seen = {}                                    # O(1) time/space - dict creation

        # Iterate through the array, tracking both current index and value
        for i, num in enumerate(nums):               # O(n) time - visits each element once
            # Calculate the value needed to reach the target sum
            complement = target - num                # O(1) time - basic arithmetic

            # Check if we've already encountered the complement value
            if complement in seen:                   # O(1) time - average hash map lookup
                # Return the stored index and current index as the solution
                return [seen[complement], i]         # O(1) time/space - list creation & return

            # Save the current number and its index for future complement checks
            seen[num] = i                            # O(1) time/space - average hash insertion

        # Fallback return (LeetCode guarantees exactly one valid pair)
        return []                                    # O(1) time/space - constant return

if __name__ == "__main__":
    # Create an instance of the solution class
    sol = Solution()                                 # O(1) time/space
    # Run test cases to verify output
    print(sol.twoSum([2, 7, 11, 15], 9))             # O(1) time - stdout print
    print(sol.twoSum([3, 2, 4], 6))                  # O(1) time - stdout print
    print(sol.twoSum([3, 3], 6))                     # O(1) time - stdout print