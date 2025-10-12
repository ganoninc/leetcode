function intToRoman(num: number): string {
  const romanNumbers = ["I", "V", "X", "L", "C", "D", "M"];
  let index = 0;
  let res = "";

  while (num > 0) {
    const digit = num % 10;

    switch (digit) {
      case 1:
        res = romanNumbers[index] + res;
        break;
      case 2:
        res = romanNumbers[index] + romanNumbers[index] + res;
        break;
      case 3:
        res =
          romanNumbers[index] + romanNumbers[index] + romanNumbers[index] + res;
        break;
      case 4:
        res = romanNumbers[index] + romanNumbers[index + 1] + res;
        break;
      case 5:
        res = romanNumbers[index + 1] + res;
        break;
      case 6:
        res = romanNumbers[index + 1] + romanNumbers[index] + res;
        break;
      case 7:
        res =
          romanNumbers[index + 1] +
          romanNumbers[index] +
          romanNumbers[index] +
          res;
        break;
      case 8:
        res =
          romanNumbers[index + 1] +
          romanNumbers[index] +
          romanNumbers[index] +
          romanNumbers[index] +
          res;
        break;
      case 9:
        res = romanNumbers[index] + romanNumbers[index + 2] + res;
        break;
      default:
        break;
    }

    index += 2;
    num = Math.floor(num / 10);
  }

  return res;
}
