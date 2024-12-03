function createHelloWorld() {
  return function (..._): string {
    return "Hello World";
  };
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
