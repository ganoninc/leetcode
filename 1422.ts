function maxScore(s: string): number {
  let onesPrefixSums: number[] = [0];
  let onesSum = 0;
  let zeroesPrefixSums: number[] = [0];
  let zeroesSum = 0;
  let maxScore = 0;

  for (let char of s) {
    if (char === "1") {
      onesSum++;
      onesPrefixSums.push(onesSum);
    } else {
      zeroesSum++;
      zeroesPrefixSums.push(zeroesSum);
    }
  }

  for (let i = 1; i < s.length; i++) {
    let leftCount = 0;
    let rightCount = 0;

    for (let j = 0; j < s.length; j++) {
      if (j < i && s[j] === "0") {
        leftCount++;
      } else if (j >= i && s[j] === "1") {
        rightCount++;
      }
    }

    // console.log(i, zeroesPrefixSums[leftCount] - zeroesPrefixSums[0]);
    // console.log("----");
    // console.log(
    //   i,
    //   onesPrefixSums[onesPrefixSums.length - 1] -
    //     onesPrefixSums[onesPrefixSums.length - rightCount - 1]
    // );

    let score =
      zeroesPrefixSums[leftCount] -
      zeroesPrefixSums[0] +
      (onesPrefixSums[onesPrefixSums.length - 1] -
        onesPrefixSums[onesPrefixSums.length - rightCount - 1]);

    maxScore = Math.max(maxScore, score);
  }

  return maxScore;
}

console.log(maxScore("011101"));

/* 

011101

011
01234

011 101

*/
