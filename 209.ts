// prefix sum approach, it works but it's too slow...
//
// function minSubArrayLen(target: number, nums: number[]): number {
//   let prefixSums: number[] = [0];
//   let sum = 0;
//   let shortestSubArray = 0;

//   for (let i = 0; i < nums.length; i++) {
//     sum += nums[i];
//     prefixSums.push(sum);

//     if (nums[i] >= target) {
//       shortestSubArray = 1;
//       return shortestSubArray;
//     }

//     let shortestSubarryForIHasBeenFound = false;
//     for (let j = i; j >= 0 && !shortestSubarryForIHasBeenFound; j--) {
//       let sumTarget = sum - target;
//       if (prefixSums[j] <= sumTarget) {
//         let subarraySum = sum - prefixSums[j];

//         if (
//           (subarraySum >= target && i - j + 1 < shortestSubArray) ||
//           (subarraySum >= target && shortestSubArray === 0)
//         ) {
//           shortestSubArray = i - j + 1;

//           if (shortestSubArray === 1) return shortestSubArray;

//           shortestSubarryForIHasBeenFound = true;
//         }
//       }
//     }
//   }

//   return shortestSubArray;
// }

// Sliding window approach
//
function minSubArrayLen(target: number, nums: number[]): number {
  if (nums.length == 0) {
    return 0;
  }

  let start = 0,
    end = 0;
  let shortestSubArrayLength = nums.length + 1;
  let sum = nums[0];

  while (
    start < nums.length &&
    end < nums.length &&
    shortestSubArrayLength > 1
  ) {
    if (sum >= target) {
      if (end - start + 1 < shortestSubArrayLength) {
        shortestSubArrayLength = end - start + 1;
      }
      sum -= nums[start];
      start++;
    } else {
      end++;
      if (end < nums.length) sum += nums[end];
      else break;
    }
  }

  if (shortestSubArrayLength == nums.length + 1) return 0;

  return shortestSubArrayLength;
}

const testArray = [2, 3, 1, 2, 4, 3];
console.log(minSubArrayLen(7, testArray));
