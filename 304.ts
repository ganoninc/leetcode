class NumMatrix {
  private prefixSumMatrix: number[][] = [];

  constructor(matrix: number[][]) {
    for (let row of matrix) {
      let prefixSums = [0];
      let sum = 0;

      for (let val of row) {
        sum += val;
        prefixSums.push(sum);
      }

      this.prefixSumMatrix.push(prefixSums);
    }
  }

  sumRegion(row1: number, col1: number, row2: number, col2: number): number {
    let res = 0;

    for (let i = row1; i <= row2; i++) {
      res += this.prefixSumMatrix[i][col2 + 1] - this.prefixSumMatrix[i][col1];
    }

    return res;
  }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */

var obj = new NumMatrix([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5],
]);
console.log(obj.sumRegion(2, 1, 4, 3));
