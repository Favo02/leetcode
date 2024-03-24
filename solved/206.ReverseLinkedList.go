package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func recursiveReverse(last, cur *ListNode) *ListNode {
	if cur == nil {
		return last
	}
	next := cur.Next
	cur.Next = last
	return recursiveReverse(cur, next)
}

func iterativeReverse(head *ListNode) *ListNode {
	var last, cur, next *ListNode
	cur = head

	for cur != nil {
		next = cur.Next
		cur.Next = last
		last = cur
		cur = next
	}

	return last
}

func reverseList(head *ListNode) *ListNode {
	// recursive:
	// return recursiveReverse(nil, head)

	// iterative:
	return iterativeReverse(head)
}
