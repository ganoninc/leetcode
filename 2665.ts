type Counter = {
  increment: () => number;
  decrement: () => number;
  reset: () => number;
};

function createCounter(init: number): Counter {
  let currentVal = init;
  return {
    increment: () => {
      currentVal++;
      return currentVal;
    },
    decrement: () => {
      currentVal--;
      return currentVal;
    },
    reset: () => {
      currentVal = init;
      return currentVal;
    },
  };
}

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
