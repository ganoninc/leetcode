function intervalIntersection(
  firstList: number[][],
  secondList: number[][]
): number[][] {
  if (firstList.length === 0 || secondList.length === 0) return [];

  let i = 0,
    j = 0;
  let res: number[][] = [];

  while (i < firstList.length && j < secondList.length) {
    if (secondList[j][0] < firstList[i][1]) {
      res.push([
        Math.max(firstList[i][0], secondList[j][0]),
        Math.min(firstList[i][1], secondList[j][1]),
      ]);

      if (secondList[j][1] >= firstList[i][1]) {
        j++;
      } else {
        i++;
      }
    } else {
      i++;
    }
  }

  return res;
}

// const mergedList = intervalIntersection(
//   [
//     [0, 2],
//     [5, 10],
//     [13, 23],
//     [24, 25],
//   ],
//   [
//     [1, 5],
//     [8, 12],
//     [15, 24],
//     [25, 26],
//   ]
// );
const mergedList = intervalIntersection(
  [
    [3, 5],
    [9, 20],
  ],
  [
    [4, 5],
    [7, 10],
    [11, 12],
    [14, 15],
    [16, 20],
  ]
);
//[[4,5],[9,10],[11,12],[14,15],[16,20]]
mergedList;
