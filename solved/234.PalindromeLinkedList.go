package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

// from LeetCode 206
func reverse(head *ListNode) *ListNode {
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

func isPalindrome(head *ListNode) bool {
	fast, slow := head, head

	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}

	slow = reverse(slow)
	for slow != nil {
		if slow.Val != head.Val {
			return false
		}
		slow = slow.Next
		head = head.Next
	}

	return true
}

func main() {
	fmt.Println(isPalindrome(&ListNode{1, &ListNode{2, &ListNode{2, &ListNode{1, nil}}}}))
	fmt.Println(isPalindrome(&ListNode{1, &ListNode{2, &ListNode{3, &ListNode{2, &ListNode{1, nil}}}}}))
}
