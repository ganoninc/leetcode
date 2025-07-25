// Time: O(n log n + m log m), where n = g.length, m = s.length
function findContentChildren(g: number[], s: number[]): number {
  const sortFunction = (a: number, b: number): number => a - b;

  g.sort(sortFunction);
  s.sort(sortFunction);

  let i = 0,
    j = 0;

  while (i < g.length && j < s.length) {
    if (g[i] <= s[j]) {
      i++;
      j++;
    } else {
      j++;
    }
  }

  return i;
}
