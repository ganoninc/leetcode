/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function (n) {
  let counter = n - 1;

  return function () {
    counter++;
    return counter;
  };
};

/**
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */

const counter = createCounter(10);
counter();
counter();
counter();
console.log(counter());