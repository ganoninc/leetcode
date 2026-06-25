class MinHeap<T> {
  private binaryTree: T[] = [];

  constructor(private comparator: (a: T, b: T) => number) {}

  private getLeftChildIndex(nodeIndex: number): number {
    return nodeIndex * 2 + 1;
  }

  private getRightChildIndex(nodeIndex: number): number {
    return nodeIndex * 2 + 2;
  }

  private getParentIndex(nodeIndex: number): number {
    return Math.floor((nodeIndex - 1) / 2);
  }

  private bubbleUp(nodeIndex: number) {
    const parentIndex = this.getParentIndex(nodeIndex);

    if (
      parentIndex >= 0 &&
      this.comparator(
        this.binaryTree[parentIndex],
        this.binaryTree[nodeIndex],
      ) > 0
    ) {
      [this.binaryTree[parentIndex], this.binaryTree[nodeIndex]] = [
        this.binaryTree[nodeIndex],
        this.binaryTree[parentIndex],
      ];
      this.bubbleUp(parentIndex);
    }
  }

  private bubbleDown(nodeIndex: number) {
    let smallestChildIndex = nodeIndex;

    const leftChildIndex = this.getLeftChildIndex(nodeIndex);
    if (
      leftChildIndex < this.binaryTree.length &&
      this.comparator(
        this.binaryTree[smallestChildIndex],
        this.binaryTree[leftChildIndex],
      ) < 0
    ) {
      smallestChildIndex = leftChildIndex;
    }

    const rightChildIndex = this.getRightChildIndex(nodeIndex);
    if (
      rightChildIndex < this.binaryTree.length &&
      this.comparator(
        this.binaryTree[smallestChildIndex],
        this.binaryTree[rightChildIndex],
      ) < 0
    ) {
      smallestChildIndex = rightChildIndex;
    }

    if (smallestChildIndex !== nodeIndex) {
      [this.binaryTree[nodeIndex], this.binaryTree[smallestChildIndex]] = [
        this.binaryTree[smallestChildIndex],
        this.binaryTree[nodeIndex],
      ];
      this.bubbleDown(smallestChildIndex);
    }
  }

  get tree(): T[] {
    return this.binaryTree;
  }

  addValue(value: T) {
    this.binaryTree.push(value);
    this.bubbleUp(this.binaryTree.length - 1);
  }

  extractMin(): T | null {
    if (this.binaryTree.length === 0) return null;

    const minValue = this.binaryTree[0];
    this.binaryTree[0] = this.binaryTree.pop();
    this.bubbleDown(0);

    return minValue;
  }
}
const numberComparator = (a: number, b: number): number => {
  return a - b;
};

const testMinHeap = new MinHeap(numberComparator);
testMinHeap.addValue(3);
testMinHeap.addValue(5);
testMinHeap.addValue(7);
testMinHeap.addValue(10);
testMinHeap.addValue(15);
testMinHeap.addValue(20);
testMinHeap.addValue(2);
console.log(testMinHeap.extractMin());

console.log(testMinHeap.tree);
