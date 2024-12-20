const ASCII_OFFSET: number = "a".charCodeAt(0);

function countGoodSubstrings(s: string): number {
  let goodSubstringCount = 0;

  if (s.length < 3) return 0;

  let letterFrequency = new Array(26).fill(0);
  let left = 0,
    right = 0;

  letterFrequency[s[right++].charCodeAt(0) - ASCII_OFFSET]++;
  letterFrequency[s[right++].charCodeAt(0) - ASCII_OFFSET]++;
  letterFrequency[s[right++].charCodeAt(0) - ASCII_OFFSET]++;

  if (
    letterFrequency[s[0].charCodeAt(0) - ASCII_OFFSET] === 1 &&
    letterFrequency[s[2].charCodeAt(0) - ASCII_OFFSET] === 1
  )
    goodSubstringCount++;

  left++;

  while (right < s.length) {
    letterFrequency[s[left - 1].charCodeAt(0) - ASCII_OFFSET]--;
    letterFrequency[s[right].charCodeAt(0) - ASCII_OFFSET]++;

    if (
      letterFrequency[s[left].charCodeAt(0) - ASCII_OFFSET] === 1 &&
      letterFrequency[s[right].charCodeAt(0) - ASCII_OFFSET] === 1
    ) {
      goodSubstringCount++;
    }

    right++;
    left++;
  }

  return goodSubstringCount;
}

console.log(countGoodSubstrings("aababcabc"));
