class NumArray {
  constructor(nums: number[], private prexfixSumArray: number[] = []) {
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
      prexfixSumArray[i] = sum + nums[i];
      sum = prexfixSumArray[i];
    }
  }

  sumRange(left: number, right: number): number {
    if (left == 0) return this.prexfixSumArray[right];

    return this.prexfixSumArray[right] - this.prexfixSumArray[left - 1];
  }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */
// -2, -2, 1, -4, -2, -3 ]
// x          x  = -1
let obj = new NumArray([-2, 0, 3, -5, 2, -1]);
var param_1 = obj.sumRange(2, 5);
