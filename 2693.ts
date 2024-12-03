type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };

interface Function {
  callPolyfill(
    context: Record<string, JSONValue>,
    ...args: JSONValue[]
  ): JSONValue;
}

Function.prototype.callPolyfill = function (context, ...args): JSONValue {
  Object.defineProperty(context, "fn", {
    value: this, // Assign the function
    enumerable: false, // Prevent it from being listed in Object.keys
    writable: true, // Allow modification if necessary
    configurable: true, // Allow deletion
  });

  let res = (context as Record<string, any>).fn(...args);

  delete context.fn;

  return res;
};

function increment() {
  this.count++;
  return this.count;
}

console.log(increment.callPolyfill({ count: 1 })); // 2
