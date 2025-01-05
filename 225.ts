class MyStack {
  private stack: number[] = [];

  constructor() {}

  push(x: number): void {
    this.stack[this.stack.length] = x;
  }

  pop(): number {
    let val = 0;

    if (!this.empty()) {
      val = this.stack[this.stack.length - 1];
      this.stack.splice(this.stack.length - 1);
    }

    return val;
  }

  top(): number {
    return this.stack.length > 0 ? this.stack[this.stack.length - 1] : 0;
  }

  empty(): boolean {
    return this.stack.length < 1;
  }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
