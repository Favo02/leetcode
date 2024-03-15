package main

import "fmt"

func productExceptSelf(nums []int) []int {
	prefix := []int{1}
	pre := nums[0]
	p := 1

	suffix := []int{1}
	suf := nums[len(nums)-1]
	s := len(nums)-2

	for i := 0; i < len(nums)-1; i++ {
		prefix = append(prefix, pre)
		pre *= nums[p]
		p++

		suffix = append(suffix, suf)
		suf *= nums[s]
		s--
	}

	res := make([]int, len(nums))
	for i, j := 0, len(nums)-1; i < len(nums); i, j = i+1, j-1 {
		res[i] = prefix[i] * suffix[j]
	}
	return res
}

func main() {
	fmt.Println(productExceptSelf([]int{1,2,3,4}))
	fmt.Println(productExceptSelf([]int{-1,1,0,-3,3}))
}
