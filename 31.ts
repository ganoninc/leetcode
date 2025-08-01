// 2   3   9   7
//     i
//             J

// 2   7   9   3
//     i
//         l   r
// 2   7   3   9

function nextPermutation(nums: number[]): void {
  // Find the first index 'i' from the right where nums[i] < nums[i + 1]
  let i = nums.length - 2;
  while (i >= 0 && nums[i] >= nums[i + 1]) {
    i--;
  }

  if (i >= 0) {
    // Find the rightmost number greater than nums[i]
    let j = nums.length - 1;
    while (nums[j] <= nums[i]) {
      j--;
    }

    // Then, we swap them
    let temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
  }

  // Reverse the subarray to the right of index i
  let left = i + 1;
  let right = nums.length - 1;
  while (left < right) {
    let temp = nums[left];
    nums[left] = nums[right];
    nums[right] = temp;
    left++;
    right--;
  }
}
