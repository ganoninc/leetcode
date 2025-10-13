function isValidSudoku(board: string[][]): boolean {
  const rowChecks = Array.from({ length: 9 }, () => new Set());
  const columnChecks = Array.from({ length: 9 }, () => new Set());
  const squareChecks = Array.from({ length: 9 }, () => new Set());

  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (board[i][j] !== ".") {
        if (rowChecks[i].has(board[i][j])) {
          return false;
        }

        if (columnChecks[j].has(board[i][j])) {
          return false;
        }

        const squareCheckIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3);
        if (squareChecks[squareCheckIndex].has(board[i][j])) {
          return false;
        }

        rowChecks[i].add(board[i][j]);
        columnChecks[j].add(board[i][j]);
        squareChecks[squareCheckIndex].add(board[i][j]);
      }
    }
  }

  return true;
}
