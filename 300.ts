function lengthOfLIS(nums: number[]): number {
  const lisList = new Array<number>(nums.length + 1);
  let max = 1;

  lisList[0] = 0;
  lisList[1] = 1;

  for (let i = 1; i < nums.length; i++) {
    const candidates = [];

    for (let j = i - 1; j >= 0; j--) {
      if (nums[j] < nums[i]) candidates.push(j);
    }

    lisList[i + 1] =
      1 + Math.max(0, ...candidates.map((index) => lisList[index + 1]));

    max = Math.max(max, lisList[i + 1]);
  }

  return max;
}

lengthOfLIS([3, 1, 8, 2, 5]);
// [0, 1, 1, 2, 2, 3];
// // lisList; // 0 1  x  x  x  x
