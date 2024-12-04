type Callback = (...args: any[]) => any;
type Subscription = {
  unsubscribe: () => void;
};

class EventEmitter {
  private subscriptions: Record<string, Callback[]> = {};

  constructor() {}

  subscribe(eventName: string, callback: Callback): Subscription {
    if (!Object.hasOwn(this.subscriptions, eventName)) {
      this.subscriptions[eventName] = [];
    }

    this.subscriptions[eventName].push(callback);

    return {
      unsubscribe: () => {
        const indexOfSubscription =
          this.subscriptions[eventName].indexOf(callback);
        if (indexOfSubscription != -1) {
          this.subscriptions[eventName].splice(indexOfSubscription, 1);
        }
        return undefined;
      },
    };
  }

  emit(eventName: string, args: any[] = []): any[] {
    let results: any[] = [];

    if (Object.hasOwn(this.subscriptions, eventName)) {
      for (let i = 0; i < this.subscriptions[eventName].length; i++) {
        results.push(this.subscriptions[eventName][i].apply(null, args));
      }
    }

    return results;
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
