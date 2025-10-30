function evalRPN(tokens: string[]): number {
  const stack: number[] = [];

  let a: number, b: number;

  for (const token of tokens) {
    switch (token) {
      case "/":
        a = stack.pop();
        b = stack.pop();
        stack.push(Math.trunc(b / a));
        break;
      case "*":
        a = stack.pop();
        b = stack.pop();
        stack.push(b * a);
        break;
      case "+":
        a = stack.pop();
        b = stack.pop();
        stack.push(b + a);
        break;
      case "-":
        a = stack.pop();
        b = stack.pop();
        stack.push(b - a);
        break;
      default:
        stack.push(parseInt(token));
    }
  }

  return stack[stack.length - 1];
}
