type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Fn = (value: JSONValue) => number;

function sortBy(arr: JSONValue[], fn: Fn): JSONValue[] {
  return arr.sort((a, b) => fn(a) - fn(b));
}

// function mergeSort(arr: number[]): number[] {
//   if (arr.length <= 1) {
//     return arr;
//   }

//   const mid = Math.floor(arr.length / 2);
//   const left = mergeSort(arr.slice(0, mid));
//   const right = mergeSort(arr.slice(mid));

//   return merge(left, right);
// }

// function merge(left: number[], right: number[]): number[] {
//   let sortedArray: number[] = [];
//   let i = 0,
//     j = 0;

//   while (i < left.length && j < right.length) {
//     if (left[i] < right[j]) {
//       sortedArray.push(left[i]);
//       i++;
//     } else {
//       sortedArray.push(right[j]);
//       j++;
//     }
//   }

//   return [...sortedArray, ...left.slice(i), ...right.slice(j)];
// }

const arr = [5, 4, 1, 2, 3];
const fn = (x) => x;
const sortedArr = sortBy(arr, fn);
sortedArr;
