/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function (nums) {
  const numCount = nums.length;
  const res = new Array(nums.length);

  const monotonicStack = [];

  for (let i = numCount * 2 - 1; i >= 0; i--) {
    const writeIndex = i % numCount;

    if (monotonicStack.length > 0) {
      while (
        monotonicStack.length > 0 &&
        monotonicStack[monotonicStack.length - 1] <= nums[i]
      ) {
        monotonicStack.pop();
      }

      if (monotonicStack.length > 0) {
        res[writeIndex] = monotonicStack[monotonicStack.length - 1];
      } else {
        res[writeIndex] = -1;
      }
    } else {
      res[writeIndex] = -1;
    }

    monotonicStack.push(nums[writeIndex]);
  }

  return res;
};

console.log(nextGreaterElements([1, 2, 3, 4, 3]));
