const arr = [1, 2, 3, 4, 5, 8, 9, 45, 77, 125];

function indexBinarySearch(
  arr: number[],
  val: number,
  left: number,
  right: number
): number {
  const mid = left + Math.floor((right - left) / 2);
  const length = right - left;

  if (length === 2) {
    return right;
  } else if (val < arr[mid]) {
    return indexBinarySearch(arr, val, left, mid);
  } else {
    return indexBinarySearch(arr, val, mid, right);
  }
}

function potentialIndexOfNewVal(arr: number[], val: number): number {
  return indexBinarySearch(arr, val, 0, arr.length - 1);
}

console.log(potentialIndexOfNewVal(arr, 10));
