function findDifference(nums1: number[], nums2: number[]): number[][] {
  const res = new Array<number[]>(2).fill([]);
  const nums1Set = new Set(nums1);
  const nums2Set = new Set(nums2);
  const res1 = new Set(nums1.filter((value) => !nums2Set.has(value)));
  const res2 = new Set(nums2.filter((value) => !nums1Set.has(value)));

  res[0] = Array.from(res1);
  res[1] = Array.from(res2);

  return res;
}
