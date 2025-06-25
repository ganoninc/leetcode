/**
 * Definition for a binary tree node.
//  * class TreeNode {
//  *     val: number
//  *     left: TreeNode | null
//  *     right: TreeNode | null
//  *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
//  *         this.val = (val===undefined ? 0 : val)
//  *         this.left = (left===undefined ? null : left)
//  *         this.right = (right===undefined ? null : right)
//  *     }
//  * }
//  */

function binaryTreePaths(root: TreeNode | null): string[] {
  const binaryTreePaths: string[] = [];

  visitNode(root, "", binaryTreePaths);

  return binaryTreePaths;
}

function visitNode(
  node: TreeNode | null,
  previousPath: string,
  binaryTreePaths: string[]
): void {
  let currentPath = previousPath + node.val.toString();

  if (node.left === null && node.right === null) {
    binaryTreePaths.push(currentPath);
  } else {
    currentPath += "->";

    if (node.left) {
      visitNode(node.left, currentPath, binaryTreePaths);
    }

    if (node.right) {
      visitNode(node.right, currentPath, binaryTreePaths);
    }
  }
}
