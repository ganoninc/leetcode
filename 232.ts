class MyQueue {
  constructor(private inbox: number[] = [], private outbox: number[] = []) {}

  push(x: number): void {
    this.inbox.push(x);
  }

  pop(): number {
    if (this.outbox.length === 0) {
      while (this.inbox.length > 0) {
        this.outbox.push(this.inbox.pop() as number);
      }
    }

    return this.outbox.pop() as number;
  }

  peek(): number {
    if (this.outbox.length === 0) {
      return this.inbox[0];
    } else {
      return this.outbox[this.outbox.length - 1];
    }
  }

  empty(): boolean {
    return this.inbox.length === 0 && this.outbox.length === 0;
  }
}
