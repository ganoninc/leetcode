function merge(intervals: number[][]): number[][] {
  if (intervals.length === 1) {
    return intervals;
  }

  const sortedIntervals = intervals.sort((a, b) => a[0] - b[0]);
  const mergedIntervals = [];

  for (let i = 0; i < sortedIntervals.length; i++) {
    let min = sortedIntervals[i][0],
      max = sortedIntervals[i][1];

    for (let j = i + 1; j < sortedIntervals.length; j++) {
      if (sortedIntervals[j][0] <= max) {
        max = Math.max(sortedIntervals[j][1], max);
        i = j;
      }
    }

    mergedIntervals.push([min, max]);
  }

  return mergedIntervals;
}

console.log(
  merge([
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18],
  ]),
);
