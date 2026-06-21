class RecentCounter {
  private data: number[] = [];
  private startIndex = 0;

  constructor() {}

  ping(t: number): number {
    this.data.push(t);

    while (this.data[this.startIndex] < t - 3000) {
      this.startIndex++;
    }

    return this.data.length - this.startIndex;
  }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */
