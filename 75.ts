/**
 Do not return anything, modify nums in-place instead.
 */

/* sorting the array with two nested loops, time complexity O(n2) space complexity, O(1) */
function sortColors(nums: number[]): void {
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[j] < nums[i]) {
        let temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
      }
    }
  }
}

/* Dutch National Flag algorithm version */
/* time complexity O(n) space complexity O(3) */

function sortColorsDNF(nums: number[]): void {
  let zeroEdge = 0,
    twoEdge = nums.length - 1,
    i = 0;

  while (i <= twoEdge) {
    if (nums[i] === 0) {
      nums[i] = nums[zeroEdge];
      nums[zeroEdge] = 0;
      i++;
      zeroEdge++;
    } else if (nums[i] === 2) {
      nums[i] = nums[twoEdge];
      nums[twoEdge] = 2;
      twoEdge--;
    } else {
      i++;
    }
  }
}
