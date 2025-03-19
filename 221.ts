function maximalSquare(matrix: string[][]): number {
  let biggestSquareSize = 0;

  let squareSizes: number[][] = new Array(matrix.length + 1)
    .fill(0)
    .map((_) => new Array(matrix[0].length + 1).fill(0));

  for (let i = 0; i < matrix[0].length; i++) {
    squareSizes[1][i + 1] = parseInt(matrix[0][i]);
    if (matrix[0][i] == "1") {
      biggestSquareSize = 1;
    }
  }

  for (let i = 1; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (matrix[i][j] === "0") {
        squareSizes[i + 1][j + 1] = 0;
      } else {
        squareSizes[i + 1][j + 1] =
          Math.min(
            squareSizes[i][j + 1],
            squareSizes[i][j],
            squareSizes[i + 1][j]
          ) + 1;

        if (squareSizes[i + 1][j + 1] > biggestSquareSize) {
          biggestSquareSize = squareSizes[i + 1][j + 1];
        }
      }
    }
  }

  return biggestSquareSize * biggestSquareSize;
}

// console.log(
//   maximalSquare([
//     ["1", "0", "1", "0", "0"],
//     ["1", "0", "1", "1", "1"],
//     ["1", "1", "1", "1", "1"],
//     ["1", "0", "0", "1", "0"],
//   ])
// );
console.log(maximalSquare([["0", "1"]]));
