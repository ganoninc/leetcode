/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function (rowsCount, colsCount) {
  if (rowsCount * colsCount !== this.length) return [];

  let twoDimensionArrayResult = [];
  let isGoingDown = true;

  let sourceArrayIndex = 0;
  for (let colsCountIndex = 0; colsCountIndex < colsCount; colsCountIndex++) {
    if (isGoingDown) {
      for (let i = 0; i < rowsCount; i++) {
        if (twoDimensionArrayResult.length < rowsCount) {
          twoDimensionArrayResult.push([]);
        }
        twoDimensionArrayResult[i].push(this[sourceArrayIndex]);
        sourceArrayIndex++;
      }
    } else {
      for (let i = rowsCount - 1; i >= 0; i--) {
        twoDimensionArrayResult[i].push(this[sourceArrayIndex]);
        sourceArrayIndex++;
      }
    }
    isGoingDown = !isGoingDown;
  }

  return twoDimensionArrayResult;
};

// const arr = [1, 2, 3, 4];
// const arr2 = arr.snail(1, 4);
// arr2;

const arr3 = [
  19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15,
];
const arr4 = arr3.snail(5, 4);
arr4;
