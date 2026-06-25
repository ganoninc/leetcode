function cancellable<T>(
  generator: Generator<Promise<any>, T, unknown>
): [() => void, Promise<T>] {
  let isCancelled = false;
  let result = generator.next();

  while (!result.done && !isCancelled) {
    if (!isCancelled) {
      result.value
        .then((value) => {
          if (!isCancelled) {
            result = generator.next(value);
          }
        })
        .catch((err) => {
          generator.throw(err);
        });
    } else {
      generator.throw("Cancelled");
    }
  }

  const promise: Promise<T> = new Promise((resolve, reject) => {
    if (!result.done) {
      resolve(result.value);
    }
  });
  return [
    () => {
      isCancelled = true;
    },
    promise,
  ];
}

function* tasks() {
  const val = yield new Promise((resolve) => resolve(2 + 2));
  yield new Promise((resolve) => setTimeout(resolve, 100));
  return val + 1;
}
const [cancel, promise] = cancellable(tasks());
setTimeout(cancel, 50);
promise.catch(console.log); // logs "Cancelled" at t=50ms
