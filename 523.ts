function checkSubarraySum(nums: number[], k: number): boolean {
  // Doesn't work
  // let moduloKsum = 0;
  // let prefixModuloKSums = new Map<number, number>();
  // prefixModuloKSums.set(0, 0);

  // for (let i = 0; i < nums.length; i++) {
  //   moduloKsum += nums[i] % k;

  //   if (i > 0 && moduloKsum % k === 0) return true;

  //   if (i > 0 && nums[i] === 0 && nums[i - 1] === 0) return true;

  //   let target = moduloKsum - k;
  //   if (prefixModuloKSums.has(target)) {
  //     return true;
  //   }

  //   prefixModuloKSums.set(moduloKsum, 0);
  // }

  if (nums.length < 2) return false;

  let remainders = new Map<number, number>();
  remainders.set(0, -1);
  let sum: number = 0;

  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];

    let remainder: number = sum % k;

    if (remainders.has(remainder)) {
      if (i - remainders.get(remainder)! > 1) return true;
    } else {
      remainders.set(remainder, i);
    }
  }

  return false;
}

// console.log(checkSubarraySum([1, 3, 6, 0, 9, 6, 93], 7));
// console.log(checkSubarraySum([1, 0], 2));
// console.log(checkSubarraySum([7, 3, 5, 2], 7));
console.log(checkSubarraySum([0, 1, 0], 1));
