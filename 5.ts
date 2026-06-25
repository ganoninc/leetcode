function longestPalindrome(s: string): string {
  let longestPalindrom = "";

  const expandAndCheckPalindrome = (left, right) => {
    while (left >= 0 && right < s.length) {
      if (s[left] === s[right]) {
        if (right - left + 1 > longestPalindrom.length) {
          longestPalindrom = s.slice(left, right + 1);
        }
        left--;
        right++;
      } else {
        break;
      }
    }
  };

  for (let i = 0; i < s.length; i++) {
    expandAndCheckPalindrome(i, i);
    expandAndCheckPalindrome(i, i + 1);
  }

  return longestPalindrom;
}

console.log(longestPalindrome("babad"));
