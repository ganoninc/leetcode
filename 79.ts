function exist(board: string[][], word: string): boolean {
  function visitLetter(
    i: number,
    j: number,
    wordIndex: number,
    alreadyVisitedLetters: Set<number>
  ) {
    if (wordIndex === word.length) return true;

    if (word[wordIndex] !== board[i][j]) return false;

    if (wordIndex === word.length - 1) return true;

    const letterKey = i * board[0].length + j;

    alreadyVisitedLetters.add(letterKey);

    if (
      i - 1 >= 0 &&
      !alreadyVisitedLetters.has((i - 1) * board[0].length + j)
    ) {
      if (visitLetter(i - 1, j, wordIndex + 1, alreadyVisitedLetters))
        return true;
    }

    if (
      i + 1 < board.length &&
      !alreadyVisitedLetters.has((i + 1) * board[0].length + j)
    ) {
      if (visitLetter(i + 1, j, wordIndex + 1, alreadyVisitedLetters))
        return true;
    }

    if (
      j - 1 >= 0 &&
      !alreadyVisitedLetters.has(i * board[0].length + (j - 1))
    ) {
      if (visitLetter(i, j - 1, wordIndex + 1, alreadyVisitedLetters))
        return true;
    }

    if (
      j + 1 < board[0].length &&
      !alreadyVisitedLetters.has(i * board[0].length + (j + 1))
    ) {
      if (visitLetter(i, j + 1, wordIndex + 1, alreadyVisitedLetters))
        return true;
    }

    alreadyVisitedLetters.delete(letterKey);

    return false;
  }

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (visitLetter(i, j, 0, new Set<number>())) {
        return true;
      }
    }
  }

  return false;
}

const board1 = [
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["A", "D", "E", "E"],
];
const word1 = "ABCCED";

console.log(exist(board1, word1));

const board2 = [["a", "b"]];
const word2 = "ba";

console.log(exist(board2, word2));
