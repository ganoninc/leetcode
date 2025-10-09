function isPowerOfTwo(n: number): boolean {
  let count = 0;

  if (n === 0) {
    return false;
  }

  while (n !== 0) {
    count += n & 1;
    if (count > 1) {
      return false;
    }
    n = n >> 1;
  }

  return true;
}
