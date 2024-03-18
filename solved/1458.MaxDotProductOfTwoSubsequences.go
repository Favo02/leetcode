package main

import (
	"fmt"
	"slices"
)

type pair struct {
	a, b int
}

func solve(nums1, nums2 []int, i, j int, mem map[pair]int) int {
	if i == len(nums1) || j == len(nums2) {
		return 0
	}

	if val, ok := mem[pair{i, j}]; ok {
		return val
	}

	res := solve(nums1, nums2, i+1, j+1, mem)
	res = max(res, nums1[i] * nums2[j] + res)
	res = max(res, solve(nums1, nums2, i+1, j, mem))
	res = max(res, solve(nums1, nums2, i, j+1, mem))

	mem[pair{i, j}] = res
	return res
}

func maxDotProduct(nums1 []int, nums2 []int) int {
	res := solve(nums1, nums2, 0, 0, make(map[pair]int))

	if res == 0 {
		res = max(slices.Max(nums1) * slices.Min(nums2), slices.Min(nums1) * slices.Max(nums2))
	}

	fmt.Println(res)
	return res
}

func main() {
	maxDotProduct([]int{2,1,-2,5}, []int{3,0,-6})
	maxDotProduct([]int{3,-2}, []int{2,-6,7})
	maxDotProduct([]int{-1,-1}, []int{1,1})
	maxDotProduct([]int{-5,-1,-2}, []int{3,3,5,5})
	maxDotProduct([]int{13,-7,12,-15,-7,8,3,-7,-5,13,-15,-8,5,7,-1,3,-11,-12,2,-12}, []int{-1,13,-4,-2,-13,2,-4,6,-9,13,-8,-3,-9})
}

