// Hashmap version
// function containsNearbyDuplicate(nums: number[], k: number): boolean {
//   let tracker: Map<number, number[]> = new Map();

//   for (let i = 0; i < nums.length; i++) {
//     if (tracker.has(nums[i])) {
//       for (let passedIndexes of tracker.get(nums[i])!) {
//         if (Math.abs(passedIndexes - i) <= k) return true;
//       }
//     } else {
//       tracker.set(nums[i], []);
//     }

//     tracker.get(nums[i])?.push(i);
//   }

//   return false;
// }

// sliding window
function containsNearbyDuplicate(nums: number[], k: number): boolean {
  let window: Set<number> = new Set();
  let left = 0;

  for (let right = 0; right < nums.length; right++) {
    if (Math.abs(left - right) > k) {
      window.delete(nums[left]);
      left++;
    }

    if (window.has(nums[right])) return true;

    window.add(nums[right]);
  }

  return false;
}

console.log(containsNearbyDuplicate([1, 2, 3, 1], 3));
