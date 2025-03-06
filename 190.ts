function reverseBits(n: number): number {
  let result = 0;
  //   console.log(n.toString(2));

  for (let i = 0; i < 32; i++) {
    result = result << 1;
    result = result | (n & 1);
    n = n >> 1;
  }

  //   console.log(result.toString(2));
  return result >>> 0;
}

reverseBits(43261596);
