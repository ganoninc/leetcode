type P = Promise<number>;

async function addTwoPromises(promise1: P, promise2: P): P {
  return new Promise((resolve, reject) => {
    Promise.all([promise1, promise2]).then((res) =>
      resolve(res.reduce((acc, elt) => acc + elt, 0))
    );
  });
}

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
