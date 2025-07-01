function intersect(nums1: number[], nums2: number[]): number[] {
  const res: number[] = [];
  const hashMap: Map<number, number> = new Map();

  let smallestArray = nums2;
  let biggestArray = nums1;

  if (nums1.length > nums2.length) {
    smallestArray = nums1;
    biggestArray = nums2;
  }

  for (let num of smallestArray) {
    let numCount = hashMap.get(num);
    if (numCount !== undefined) {
      hashMap.set(num, numCount + 1);
    } else {
      hashMap.set(num, 1);
    }
  }

  for (let num of biggestArray) {
    let numCount = hashMap.get(num);
    if (numCount !== undefined && numCount > 0) {
      res.push(num);
      hashMap.set(num, numCount - 1);
    }
  }

  return res;
}
