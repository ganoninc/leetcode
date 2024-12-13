// Hashmap version
function containsNearbyDuplicate(nums: number[], k: number): boolean {
  let tracker: Map<number, number[]> = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (tracker.has(nums[i])) {
      for (let passedIndexes of tracker.get(nums[i])!) {
        if (Math.abs(passedIndexes - i) <= k) return true;
      }
    } else {
      tracker.set(nums[i], []);
    }

    tracker.get(nums[i])?.push(i);
  }

  return false;
}

console.log(containsNearbyDuplicate([1, 2, 3, 1], 3));
