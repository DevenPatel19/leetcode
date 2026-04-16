
// Case 1

nums1 = [2,7,11,15]
target1 =9
Expected1 = [0,1]
// Case 2
nums2 = [3,2,4]
target2 = 6
Expected2 = [1,2]

// Case 3
nums3 = [3,3]
target3 = 6
Expected3 = [0,1]


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let ans = []  // to store the indices of the two numbers
    for (i=0; i < nums.length; i++){  // loop through each element in the array
        for (let j = i + 1; j < nums.length; j++) { // loop through the rest of the array to find the other number
        let sum = nums[i] + nums[j]; // calculate the sum of the two numbers
        if (sum === target) { // check if the sum equals the target value
        ans.push(i); // store the indices of the two numbers
        ans.push(j);
        return ans; // return the answer
      }
    }
  }
  return ans; // if no such numbers exist, return an empty vector
}



console.log(twoSum(nums1, target1));
console.log("expected " + Expected1)

console.log(twoSum(nums2, target2));
console.log("expected " + Expected2)


console.log(twoSum(nums3, target3));
console.log("expected " + Expected3)

