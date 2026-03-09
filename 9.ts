function isPalindrome(x: number): boolean {
  if (x < 0) {
    return false;
  }

  let copyOfX = x;
  let reversedX = 0;

  while (copyOfX > 0) {
    let unitsDigit = copyOfX % 10;
    reversedX = reversedX * 10 + unitsDigit;
    copyOfX = Math.floor(copyOfX / 10);
  }

  return x === reversedX;
}

console.log(isPalindrome(121));
