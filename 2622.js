var TimeLimitedCache = function () {
  this.itemMap = new Map();
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
  if (this.itemMap.has(key)) {
    const entry = this.itemMap.get(key);
    const isPreviousEntryExpired = entry.expirationTimestamp <= Date.now();

    entry.expirationTimestamp = Date.now() + duration;
    entry.value = value;

    return !isPreviousEntryExpired;
  } else {
    this.itemMap.set(key, {
      expirationTimestamp: Date.now() + duration,
      value: value,
    });

    return false;
  }
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
  if (!this.itemMap.has(key)) return -1;

  const entry = this.itemMap.get(key);

  if (entry.expirationTimestamp <= Date.now()) return -1;

  return entry.value;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
  let keyCount = 0;
  const currentDate = Date.now();

  for (const [_, value] of this.itemMap) {
    if (value.expirationTimestamp > currentDate) {
      keyCount++;
    }
  }

  return keyCount;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */

// Create the cache
const cache = new TimeLimitedCache();

// Test set method
console.log(cache.set(1, 100, 1000)); // false (new key)
console.log(cache.set(1, 200, 1000)); // true (key already existed and is not expired)

// Test get method
console.log(cache.get(1)); // 200 (value exists and is not expired)

// Wait for 1.5 seconds to test expiration
setTimeout(() => {
  console.log(cache.get(1)); // -1 (key is expired)
}, 1500);

// Test count method with multiple keys
cache.set(2, 300, 2000);
cache.set(3, 400, 3000);
console.log(cache.count()); // 2 (both keys are valid)

// Wait for 2.5 seconds and check count again
setTimeout(() => {
  console.log(cache.count()); // 1 (one key expired)
}, 2500);
