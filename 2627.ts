type F = (...args: any[]) => void;

function debounce(fn: F, t: number): F {
  let timeoutId: number | NodeJS.Timeout | undefined;
  return function (...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn(...args), t);
  };
}

const log = debounce(console.log, 100);
log("Hello"); // cancelled
log("Hello"); // cancelled
log("Hello"); // Logged at t=100ms
