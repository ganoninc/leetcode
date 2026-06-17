function uniqueOccurrences(arr: number[]): boolean {
  const numberIndex = new Map<number, number[]>();

  for (let i = 0; i < arr.length; i++) {
    if (!numberIndex.has(arr[i])) {
      numberIndex.set(arr[i], []);
    }

    numberIndex.get(arr[i]).push(i);
  }

  const frequencySet = new Set<number>();

  for (const [key, value] of numberIndex) {
    if (frequencySet.has(value.length)) {
      return false;
    }

    frequencySet.add(value.length);
  }

  return true;
}
