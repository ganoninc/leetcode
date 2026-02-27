function canPartition(nums: number[]): boolean {
  const memo = new Map<string, boolean>();

  const total = nums.reduce((acc: number, num: number) => {
    return acc + num;
  }, 0);

  if (total % 2 !== 0) {
    return false;
  }

  const target = total / 2;

  function dfs(index: number, sum: number) {
    const key = `${index}-${sum}`;

    if (memo.has(key)) return memo.get(key);

    if (sum === target) return true;
    if (index >= nums.length || sum > target) return false;

    const result = dfs(index + 1, sum + nums[index]) || dfs(index + 1, sum);

    memo.set(key, result);

    return result;
  }

  return dfs(0, 0);
}
