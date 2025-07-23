/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  const res = [];

  let prevValue = null;

  for (let i = 0; i < nums.length - 2; i++) {
    if (prevValue === nums[i]) continue;

    prevValue = nums[i];

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (sum === 0) {
        res.push([nums[i], nums[left], nums[right]]);
        while (left < right && nums[left] === nums[left + 1]) {
          left++;
        }
        while (left < right && nums[right] === nums[right - 1]) {
          right--;
        }

        left++;
        right--;
      } else if (sum < 0) {
        while (left < right && nums[left] === nums[left + 1]) {
          left++;
        }
        left++;
      } else {
        while (left < right && nums[right] === nums[right - 1]) {
          right--;
        }
        right--;
      }
    }
  }

  return res;
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
