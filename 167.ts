function twoSum(numbers: number[], target: number): number[] {
  for (let i = 0; i < numbers.length - 1; i++) {
    const complementIndex = binarySearch(
      i + 1,
      numbers.length - 1,
      target - numbers[i],
      numbers
    );

    if (complementIndex !== -1) {
      return [i + 1, complementIndex + 1];
    }
  }
}

function binarySearch(
  start: number,
  end: number,
  target: number,
  numbers: number[]
): number {
  if (start <= end) {
    const middle = Math.floor((start + end) / 2);

    if (numbers[middle] === target) {
      return middle;
    } else if (numbers[middle] >= target) {
      return binarySearch(start, middle - 1, target, numbers);
    } else if (numbers[middle] <= target) {
      return binarySearch(middle + 1, end, target, numbers);
    }
  } else {
    return -1;
  }
}
