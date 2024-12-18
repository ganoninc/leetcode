// function* codeGenerator(
//   nums: number[],
//   startIndex,
//   isBackward = false
// ): Generator<number, boolean, number> {
//   if (nums.length === 0) {
//     return false;
//   }

//   let i = startIndex;
//   if (i > nums.length - 1) {
//     i = 0;
//   }
//   //   i = isBackward ? (i === 0 ? nums.length - 1 : i - 1) : (i + 1) % nums.length;

//   while (true) {
//     yield nums[i];
//     i = isBackward
//       ? i === 0
//         ? nums.length - 1
//         : i - 1
//       : (i + 1) % nums.length;
//   }
// }

function decrypt(code: number[], k: number): number[] {
  if (k === 0) {
    return Array(code.length).fill(0);
  }

  const n = code.length;
  const res: number[] = [];
  let windowValue = 0;

  if (k > 0) {
    for (let i = 1; i <= k; i++) {
      windowValue += code[i % n];
    }
    res.push(windowValue);

    for (let i = 1; i < n; i++) {
      windowValue -= code[i];
      windowValue += code[(i + k) % n];
      res.push(windowValue);
    }
  } else {
    for (let i = 1; i <= -k; i++) {
      windowValue += code[n - i];
    }
    res.push(windowValue);

    for (let i = 1; i < n; i++) {
      const removeIndex = (i - 1 - -k + n) % n;
      const addIndex = (i - 1 + n) % n;

      windowValue -= code[removeIndex];
      windowValue += code[addIndex];
      res.push(windowValue);
    }
  }

  return res;
}

// console.log(decrypt([5, 7, 1, 4], 3));
console.log(decrypt([10, 5, 7, 7, 3, 2, 10, 3, 6, 9, 1, 6], -4));
