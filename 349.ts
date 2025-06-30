function intersection(nums1: number[], nums2: number[]): number[] {
  const res: number[] = [];
  const nums1UniqueValues: boolean[] = new Array(1001);

  nums1.forEach((num) => {
    nums1UniqueValues[num] = true;
  });

  for (let num of nums2) {
    if (nums1UniqueValues[num]) {
      res.push(num);
      nums1UniqueValues[num] = false;
    }
  }

  return res;
}
