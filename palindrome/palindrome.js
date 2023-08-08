// Test Cases
// Case 1
x1 = 121
e1 = "true"
// Case 2
x2 = -121
e2 = "false"
// Case 3
x3 = 10
e3 = "false"

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const str = x.toString();
  let leftIndex = 0;
  let rightIndex = str.length - 1;

  while (leftIndex < rightIndex) {
    if (str.charAt(leftIndex) !== str.charAt(rightIndex)) {
      return false;
    }
    leftIndex++;
    rightIndex--;
  }

  return true;
}


    console.log(isPalindrome(x1))
    console.log( "expected " + e1 )
    
    
    console.log(isPalindrome(x1))
    console.log( "expected " + e2 )

    
    console.log(isPalindrome(x1))
    console.log( "expected " + e3 )
