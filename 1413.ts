function minStartValue(nums: number[]): number {
  let sum = 0;
  let lowestElt = nums[0];

  for (let num of nums) {
    sum += num;
    if (sum < lowestElt) {
      lowestElt = sum;
    }
  }

  if (lowestElt > 0) {
    return 1;
  } else {
    return 1 + Math.abs(lowestElt);
  }
}

const arr = [-3, 2, -3, 4, 2];
console.log(minStartValue(arr));
