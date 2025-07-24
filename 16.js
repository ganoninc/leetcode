/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
  nums.sort((a, b) => a - b); // O(n log n)
  let closestSumToTarget = nums[0] + nums[1] + nums[2];

  for (let i = 0; i < nums.length - 2; i++) {
    let left = i + 1,
      right = nums.length - 1;

    while (left < right) {
      let sum = nums[i] + nums[left] + nums[right];

      if (Math.abs(target - sum) < Math.abs(target - closestSumToTarget)) {
        closestSumToTarget = sum;
      }

      if (sum < target) {
        while (left < right && nums[left + 1] === nums[left]) {
          left++;
        }
        left++;
      } else if (sum > target) {
        while (left < right && nums[right - 1] === nums[right]) {
          right--;
        }
        right--;
      } else {
        return closestSumToTarget;
      }
    }
  }

  return closestSumToTarget;
};

// console.log(threeSumClosest([-1, 2, 1, -4], 1));
// console.log(threeSumClosest([1, 1, 1, 0], 100));
console.log(threeSumClosest([1, 2, 7, 13], 12));
