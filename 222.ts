class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function doesNodeExist(
  root: TreeNode | null,
  index: number,
  levelCount: number
): boolean {
  const indexAsBinary: string = index.toString(2).padStart(levelCount - 1, "0");
  let nodeToVisit: TreeNode | null = root;

  for (const bit of indexAsBinary) {
    if (bit === "0") {
      nodeToVisit = nodeToVisit?.left || null;
    } else {
      nodeToVisit = nodeToVisit?.right || null;
    }
  }

  return nodeToVisit != null;
}

function countNodes(root: TreeNode | null): number {
  if (!root) return 0;

  let levelCount: number = 0;
  let nodeToVisit: TreeNode | null = root;

  while (nodeToVisit != null) {
    levelCount++;
    nodeToVisit = nodeToVisit.left;
  }

  let left = 0,
    right = Math.pow(2, levelCount - 1) - 1;

  let lastPopulatedNode: number = 0; // the first node of a level will always be populated

  while (left <= right) {
    let nodeToCheckIndex = Math.floor((left + right) / 2);

    if (doesNodeExist(root, nodeToCheckIndex, levelCount)) {
      left = nodeToCheckIndex + 1;
      lastPopulatedNode = nodeToCheckIndex;
    } else {
      right = nodeToCheckIndex - 1;
    }
  }

  return Math.pow(2, levelCount - 1) - 1 + lastPopulatedNode + 1;
}

function arrayToTree(arr: number[]): TreeNode | null {
  if (arr.length === 0) return null;

  let root = new TreeNode(arr[0]);
  let queue: TreeNode[] = [root];
  let i = 1;

  while (i < arr.length) {
    let current = queue.shift()!; // Get the front of the queue

    if (i < arr.length) {
      current.left = new TreeNode(arr[i++]);
      queue.push(current.left);
    }

    if (i < arr.length) {
      current.right = new TreeNode(arr[i++]);
      queue.push(current.right);
    }
  }

  return root;
}

// Example Usage:
const root = arrayToTree([1, 2, 3, 4, 5, 6]);
console.log(countNodes(root));
