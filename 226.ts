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

// Recrusive version
// function permuteChildren(node: TreeNode | null): void {
//   if (node !== null) {
//     const leftChild = node.left;
//     node.left = node.right;
//     node.right = leftChild;

//     permuteChildren(node.left);
//     permuteChildren(node.right);
//   }
// }

// function invertTree(root: TreeNode | null): TreeNode | null {
//   if (root === null) return root;
//   permuteChildren(root);
//   return root;
// }

// iterative version

function invertTree(root: TreeNode | null): TreeNode | null {
  if (root === null) return root;
  return root;
}
