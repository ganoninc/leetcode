type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (
  arr: MultiDimensionalArray,
  n: number
): MultiDimensionalArray {
  return flattenArray(arr, n, 0);
};

var flattenArray = function (
  arr: MultiDimensionalArray,
  n: number,
  currentDepth: number
): MultiDimensionalArray {
  if (currentDepth >= n) return arr;

  let result: MultiDimensionalArray = [];

  for (let i = 0; i < arr.length; i++) {
    if (Array.isArray(arr[i])) {
      result.push(
        ...flattenArray(arr[i] as MultiDimensionalArray, n, currentDepth + 1)
      );
    } else {
      result.push(arr[i]);
    }
  }
  return result;
};

const arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]];
console.log(flat(arr, 2));
