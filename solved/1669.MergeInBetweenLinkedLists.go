package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeInBetween(list1 *ListNode, a int, b int, list2 *ListNode) *ListNode {
	var pre, post *ListNode

	cur := list1
	for i := 0; i <= b; i++ {
		if i == a-1 {
			pre = cur
		}
		cur = cur.Next
	}
	post = cur

	pre.Next = list2

	cur = pre
	for cur.Next != nil {
		cur = cur.Next
	}
	cur.Next = post

	return list1
}

func main() {
	fmt.Println(mergeInBetween(&ListNode{10, &ListNode{1, &ListNode{13, &ListNode{6, &ListNode{9, &ListNode{5, nil}}}}}}, 3, 4, &ListNode{1000000, &ListNode{1000001, &ListNode{1000002, nil}}}))
}
