function sumOddLengthSubarrays(arr: number[]): number {
  // calculate prefix sums
  // find each candidate and compute their sum
  // add all the sums together

  let sumOfOddLengthSubarrays = 0;

  let prefixSums: number[] = [0];
  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
    prefixSums.push(sum);
    sumOfOddLengthSubarrays += arr[i];
  }

  let length = 3;
  while (length <= arr.length) {
    for (let i = 0; i + length - 1 < arr.length; i++) {
      sumOfOddLengthSubarrays += prefixSums[i + length] - prefixSums[i];
    }
    length += 2;
  }

  return sumOfOddLengthSubarrays;
}

console.log(sumOddLengthSubarrays([1, 4, 2, 5, 3]));
