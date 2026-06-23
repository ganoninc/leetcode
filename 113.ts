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

function pathSum(root: TreeNode | null, targetSum: number): number[][] {
  const res: number[][] = [];

  const dfs = (
    node: TreeNode | null,
    ancestors: number[],
    targetSum: number,
  ) => {
    if (!node) {
      return;
    }

    const currentPath = [...ancestors, node.val];
    const currentTargetSum = targetSum - node.val;

    if (!node.left && !node.right && currentTargetSum == 0) {
      res.push(currentPath);
      return;
    }

    dfs(node.left, currentPath, currentTargetSum);
    dfs(node.right, currentPath, currentTargetSum);
  };

  dfs(root, [], targetSum);

  return res;
}
