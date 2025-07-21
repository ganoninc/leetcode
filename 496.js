/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function (nums1, nums2) {
  const nextGreaterElements = new Map();
  let monotonicStack = [];

  for (let i = nums2.length - 1; i >= 0; i--) {
    if (monotonicStack.length === 0) {
      nextGreaterElements.set(nums2[i], -1);
    } else {
      while (
        monotonicStack.length > 0 &&
        nums2[monotonicStack[monotonicStack.length - 1]] < nums2[i]
      ) {
        monotonicStack.pop();
      }

      if (monotonicStack.length === 0) {
        nextGreaterElements.set(nums2[i], -1);
      } else {
        nextGreaterElements.set(
          nums2[i],
          nums2[monotonicStack[monotonicStack.length - 1]]
        );
      }
    }

    monotonicStack.push(i);
  }

  return nums1.map((elt) => nextGreaterElements.get(elt));
};

console.log(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]));
