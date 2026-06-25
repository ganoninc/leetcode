function numIslands(grid: string[][]): number {
  let islandCount = 0;
  const visited = Array.from({ length: grid.length }, () =>
    Array.from({ length: grid[0].length }, () => false),
  );

  const isOutOfBound = (i, j) => {
    return i < 0 || i >= grid.length || j < 0 || j >= grid[0].length;
  };

  const isLand = (i, j) => {
    return grid[i][j] === "1";
  };

  const directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
  ];

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (!visited[i][j] && isLand(i, j)) {
        const stack = [[i, j]];
        visited[i][j] = true;
        islandCount++;

        while (stack.length > 0) {
          let current = stack.pop();

          for (const direction of directions) {
            const [dx, dy] = direction;
            const x = current[0] + dx;
            const y = current[1] + dy;

            if (!isOutOfBound(x, y) && !visited[x][y] && isLand(x, y)) {
              stack.push([x, y]);
              visited[x][y] = true;
            }
          }
        }
      }
    }
  }

  return islandCount;
}

console.log(
  numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
  ]),
);
