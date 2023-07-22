/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  const n1 = linkedListToInt(l1)
  const n2 = linkedListToInt(l2)
  return intToLinkedList(n1 + n2)
}

function linkedListToInt(l) {
  let n = []
  for (var i = 0; l.next; i++) {
    n.push(l.val)
    l = l.next
  }
  n.push(l.val)
  return BigInt(n.reverse().join(""))
}

function intToLinkedList(n) {
  const head = {}
  let cur = head

  while (n > 9) {
    cur.val = n % 10n
    cur.next = {}
    n = n / 10n

    cur = cur.next
  }

  cur.val = n % 10n
  cur.next = null

  return head
}
