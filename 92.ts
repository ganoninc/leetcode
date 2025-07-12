// class ListNode {
//   val: number;
//   next: ListNode | null;
//   constructor(val?: number, next?: ListNode | null) {
//     this.val = val === undefined ? 0 : val;
//     this.next = next === undefined ? null : next;
//   }
// }

function reverseBetween(
  head: ListNode | null,
  left: number,
  right: number
): ListNode | null {
  if (head!.next === null || left === right) {
    return head;
  }

  let dummyNode = new ListNode(0, head);
  let nodeBeforeLeft: ListNode | null = dummyNode;

  let nodeAfterRight: ListNode | null = null;

  let i = 0;
  let current = nodeBeforeLeft.next;
  while (i < left - 1) {
    nodeBeforeLeft = current;
    current = nodeBeforeLeft!.next;
    i++;
  }

  let lastNodeOfReversedSubListNode = current;

  let prev: ListNode | null = null;
  while (i < right) {
    let nextNode = current!.next;
    current!.next = prev;
    prev = current;
    current = nextNode;
    i++;
  }

  nodeAfterRight = current;

  nodeBeforeLeft!.next = prev;

  lastNodeOfReversedSubListNode!.next = nodeAfterRight;

  return dummyNode.next;
}
