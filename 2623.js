/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
  let cache = {};
  return function (...args) {
    const callHash = JSON.stringify(args);

    if (!cache.hasOwnProperty(callHash)) {
      cache[callHash] = fn(...args);
    }

    return cache[callHash];
  };
}

let callCount = 0;
const memoizedFn = memoize(function (a, b) {
  callCount += 1;
  return a + b;
});
memoizedFn(2, 3); // 5
memoizedFn(2, 3); // 5
console.log(callCount); // 1
