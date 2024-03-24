package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reorderList(head *ListNode) {
	if head == nil || head.Next == nil {
		return
	}

	arr := make([]int, 0)
	cur := head
	for cur != nil {
		arr = append(arr, cur.Val)
		cur = cur.Next
	}

	head.Next = &ListNode{arr[len(arr)-1], nil}
	cur = head.Next

	for i := 1; i < len(arr)/2; i++ {
		cur.Next = &ListNode{arr[i], nil}
		cur = cur.Next
		cur.Next = &ListNode{arr[len(arr)-1-i], nil}
		cur = cur.Next
	}
	if len(arr)%2 == 1 {
		cur.Next = &ListNode{arr[len(arr)/2], nil}
	}
}
