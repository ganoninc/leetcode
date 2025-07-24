function isHappy(n: number): boolean {
  const sumOfSquaresMap: Map<number, number> = new Map<number, number>();
  while (true) {
    if (sumOfSquaresMap.has(n)) {
      return false;
    }

    let sumOfSquares = 0;
    let num = n;
    while (num > 0) {
      let digit = num % 10;
      sumOfSquares += Math.pow(digit, 2);
      num = Math.floor(num / 10);
    }

    if (sumOfSquares === 1) {
      return true;
    }

    sumOfSquaresMap.set(n, sumOfSquares);

    n = sumOfSquares;
  }
}
