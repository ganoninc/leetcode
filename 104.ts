/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;

  let maxDepth = 0;

  const getMaxDepth = (node: TreeNode, depth: number) => {
    maxDepth = Math.max(maxDepth, depth);
    if (node.left) {
      getMaxDepth(node.left, depth + 1);
    }
    if (node.right) {
      getMaxDepth(node.right, depth + 1);
    }
  };

  getMaxDepth(root, 1);

  return maxDepth;
}
