function closeStrings(word1: string, word2: string): boolean {
  const word1LetterCountMap = new Map<string, number>();
  const word2LetterCountMap = new Map<string, number>();

  for (const letter of word1) {
    word1LetterCountMap.set(letter, (word1LetterCountMap.get(letter) || 0) + 1);
  }

  for (const letter of word2) {
    word2LetterCountMap.set(letter, (word2LetterCountMap.get(letter) || 0) + 1);
  }

  //   1st we check if word1 and word2 are made with exactly the same set of letters
  for (const letter of word1LetterCountMap.keys()) {
    if (!word2LetterCountMap.has(letter)) return false;
  }
  for (const letter of word2LetterCountMap.keys()) {
    if (!word1LetterCountMap.has(letter)) return false;
  }

  //   2nd we make sure their letter frequencies match, regardless of the letter (eg. aaa == ccc, bb == aa, c == b, meaning a frequency of 3, 2, and 1)
  const sortedWord1Frequencies = [...word1LetterCountMap.values()].sort(
    (a, b) => a - b,
  );
  const sortedWord2Frequencies = [...word2LetterCountMap.values()].sort(
    (a, b) => a - b,
  );

  if (sortedWord1Frequencies.length !== sortedWord2Frequencies.length) {
    return false;
  }

  for (let i = 0; i < sortedWord1Frequencies.length; i++) {
    if (sortedWord1Frequencies[i] !== sortedWord2Frequencies[i]) {
      return false;
    }
  }

  return true;
}

closeStrings("abbzccca", "babzzczc");
