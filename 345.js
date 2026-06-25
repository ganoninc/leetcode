/**
 * @param {string} s
 * @return {string}
 */
const reverseVowels = function (s) {
  let left = 0,
    right = s.length - 1;

  while (left < right) {
    if (isEnglishVowel(s.charAt(left)) && isEnglishVowel(s.charAt(right))) {
      let temp = s.charAt(left);
      s.replaceAt(left, s.charAt(right));
      s.replaceAt(right, temp);

      left++;
      right--;
    } else if (isEnglishVowel(s.charAt(left))) {
      right--;
    } else {
      left++;
    }
  }

  return s;
};

/**
 * @param {string} c
 * @return {boolean}
 */
const isEnglishVowel = function (c) {
  switch (c) {
    case "a":
      return true;
    case "A":
      return true;
    case "e":
      return true;
    case "E":
      return true;
    case "i":
      return true;
    case "I":
      return true;
    case "o":
      return true;
    case "O":
      return true;
    case "u":
      return true;
    case "U":
      return true;
    default:
      return false;
  }
};

String.prototype.replaceAt = function (index, char) {
  return this.substring(0, index) + char + this.substring(index + 1);
};

reverseVowels("IceCreAm");
