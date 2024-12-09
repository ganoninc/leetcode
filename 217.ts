function containsDuplicate(nums: number[]): boolean {
  let map = new Map<number, number>();

  for (let num of nums) {
    if (map.has(num)) {
      return true;
    }
    map.set(num, 0);
  }

  return false;
}
