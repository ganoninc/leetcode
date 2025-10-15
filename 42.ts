function trap(height: number[]): number {
  if (height.length < 3) {
    return 0;
  }

  const previousGreatest: number[] = new Array(height.length).fill(0);
  const nextGreatest: number[] = new Array(height.length).fill(0);

  for (let i = 1; i < height.length; i++) {
    if (height[i - 1] > previousGreatest[i - 1]) {
      previousGreatest[i] = height[i - 1];
    } else {
      previousGreatest[i] = previousGreatest[i - 1];
    }
  }

  for (let i = height.length - 2; i >= 0; i--) {
    if (height[i + 1] > nextGreatest[i + 1]) {
      nextGreatest[i] = height[i + 1];
    } else {
      nextGreatest[i] = nextGreatest[i + 1];
    }
  }

  let totalTrappedWater = 0;

  for (let i = 1; i < height.length - 1; i++) {
    const trappedWatter =
      Math.min(previousGreatest[i], nextGreatest[i]) - height[i];
    if (trappedWatter > 0) {
      totalTrappedWater += trappedWatter;
    }
  }

  return totalTrappedWater;
}

console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));
