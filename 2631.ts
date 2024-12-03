interface Array<T> {
  groupBy(fn: (item: T) => string): Record<string, T[]>;
}

Array.prototype.groupBy = function (fn) {
  let groupedArray = {};

  for (let elt of this) {
    let key = fn(elt);

    if (!groupedArray.hasOwnProperty(key)) groupedArray[key] = [];

    groupedArray[key].push(elt);
  }

  return groupedArray;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
