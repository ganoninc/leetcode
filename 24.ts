/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function swapPairs(head: ListNode | null): ListNode | null {
  if (!head || !head.next) return head;

  let dummyNode: ListNode = new ListNode(0, head);

  let nodeBeforePair = dummyNode;
  let nodeAfterPair: ListNode | null = null;

  let current = dummyNode.next;

  while (current && current.next) {
    nodeAfterPair = current.next.next;
    let nodeA = current;
    let nodeB = current.next;

    nodeBeforePair.next = nodeB;
    nodeB.next = nodeA;
    nodeA.next = nodeAfterPair;

    current = nodeAfterPair;
    nodeBeforePair = nodeA;
  }

  return dummyNode.next;
}
