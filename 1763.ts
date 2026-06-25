const asciiStartIndex = "A".charCodeAt(0);
const lowercaseOffset = "a".charCodeAt(0) - asciiStartIndex;

function isNiceSubstring(letterSet: Set<string>): boolean {
  for (let letter of letterSet) {
    if (letter.charCodeAt(0) >= "a".charCodeAt(0)) {
      if (
        !letterSet.has(
          String.fromCharCode(letter.charCodeAt(0) - lowercaseOffset)
        )
      ) {
        return false;
      }
    } else {
      if (
        !letterSet.has(
          String.fromCharCode(letter.charCodeAt(0) + lowercaseOffset)
        )
      ) {
        return false;
      }
    }
  }

  return true;
}

function longestNiceSubstring(s: string): string {
  let letterSet: Set<string> = new Set();
  let start = 0;
  let end = 0;

  while (end < s.length) {
    letterSet.add(s[end]);
    if (isNiceSubstring(letterSet)) {
      return s.slice(start, end + 1);
    } else {
      end++;
    }
  }

  while (start < s.length - 1) {
    letterSet.delete(s[start]);
    if (isNiceSubstring(letterSet)) {
      return s.slice(start + 1, end + 1);
    } else {
      start++;
    }
  }

  return "";
}

console.log(longestNiceSubstring("YazaAay"));
