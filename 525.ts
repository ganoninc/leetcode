function findMaxLength(nums: number[]): number {
  let maxLength = 0;
  let sumMap = new Map();
  let sum = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] == 0) {
      sum--;
    } else {
      sum++;
    }

    if (!sumMap.get(sum)) sumMap.set(sum, []);

    sumMap.get(sum).push(i);

    if (sum == 0) {
      if (i + 1 > maxLength) maxLength = i + 1;
    } else {
      if (sumMap.get(sum).length > 1) {
        let candidateMaxLenght =
          sumMap.get(sum)[sumMap.get(sum).length - 1] - sumMap.get(sum)[0];

        if (candidateMaxLenght > maxLength) maxLength = candidateMaxLenght;
      }
    }
  }
  return maxLength;
}

console.log(findMaxLength([0, 1])); // Output: 2
console.log(findMaxLength([0, 0, 0, 1, 1, 1, 1])); // Output: 6
console.log(findMaxLength([0, 1, 0, 1, 1, 0, 0])); // Output: 6
console.log(findMaxLength([0, 0, 0, 0, 0])); // Output: 0
console.log(findMaxLength([0, 1, 0, 1, 0, 1, 0, 1])); // Output: 8
console.log(findMaxLength([1, 1, 1, 0, 0, 0, 0, 1])); // Output: 8
console.log(findMaxLength([0, 1, 0, 1, 1, 1, 0, 0, 1, 0])); // Output: 10
console.log(findMaxLength([0, 1, 0, 1])); // Output: 4
console.log(findMaxLength([1, 1, 1, 1, 0, 0, 0, 0])); // Output: 8
console.log(findMaxLength([0, 1])); // Output: 2
