function twoSum(nums: number[], target: number): number[] {
  let hashmap: Map<number, number> = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    if (hashmap.has(target - nums[i])) {
      return [hashmap.get(target - nums[i]) as number, i];
    }
    hashmap.set(nums[i], i);
  }
}

console.log(twoSum([2, 7, 11, 15], 9));
