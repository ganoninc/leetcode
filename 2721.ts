type Fn<T> = () => Promise<T>;

function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {
  let results: T[] = [];
  let resolvedPromiseCount = 0;

  return new Promise((resolve, reject) => {
    functions.forEach((fn, i) => {
      fn()
        .then((res: T) => {
          results[i] = res;
          resolvedPromiseCount++;
          if (resolvedPromiseCount == functions.length) {
            resolve(results);
          }
        })
        .catch((err) => {
          reject(err);
        });
    });
  });
}

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
