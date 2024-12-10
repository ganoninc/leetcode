function pivotIndex(nums: number[]): number {
  let sum = 0;
  let prefixSums = [0];

  for (let num of nums) {
    sum += num;
    prefixSums.push(sum);
  }

  for (let i = 0; i < nums.length; i++) {
    let sumBefore = prefixSums[i];
    let sumAfter = prefixSums[prefixSums.length - 1] - prefixSums[i + 1];

    if (sumBefore == sumAfter) {
      return i;
    }
  }

  return -1;
}

const arr = [1, 7, 3, 6, 5, 6];
console.log(pivotIndex(arr));
