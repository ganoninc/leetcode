function addDigits(num: number): number {
  while (num > 9) {
    const numAsString = num.toString();
    let newNum = 0;

    for (const digit of numAsString) {
      newNum += parseInt(digit);
    }

    num = newNum;
  }

  return num;
}
