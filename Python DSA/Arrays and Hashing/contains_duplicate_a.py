"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List

# ============================================================
# TODO: Write your solution inside this function
# ============================================================
def containsDuplicate(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False
# ============================================================

# Test cases
nums1 = [1, 2, 3, 1]
expected1 = True

nums2 = [1, 2, 3, 4]
expected2 = False

nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
expected3 = True

nums4 = []
expected4 = False

nums5 = [42]
expected5 = False

# Run tests
print("Running tests for containsDuplicate...\n")

result1 = containsDuplicate(nums1)
print(f"Input: {nums1}")
print(f"Output: {result1}")
print(f"Expected: {expected1}")
print(f"{'✓ PASS' if result1 == expected1 else '✗ FAIL'}\n")

result2 = containsDuplicate(nums2)
print(f"Input: {nums2}")
print(f"Output: {result2}")
print(f"Expected: {expected2}")
print(f"{'✓ PASS' if result2 == expected2 else '✗ FAIL'}\n")

result3 = containsDuplicate(nums3)
print(f"Input: {nums3}")
print(f"Output: {result3}")
print(f"Expected: {expected3}")
print(f"{'✓ PASS' if result3 == expected3 else '✗ FAIL'}\n")

result4 = containsDuplicate(nums4)
print(f"Input: {nums4}")
print(f"Output: {result4}")
print(f"Expected: {expected4}")
print(f"{'✓ PASS' if result4 == expected4 else '✗ FAIL'}\n")

result5 = containsDuplicate(nums5)
print(f"Input: {nums5}")
print(f"Output: {result5}")
print(f"Expected: {expected5}")
print(f"{'✓ PASS' if result5 == expected5 else '✗ FAIL'}\n")