package main

import "fmt"

func firstMissingPositive(nums []int) int {
	OUT := len(nums) + 1

	for i, n := range nums {
		if n <= 0 {
			nums[i] = OUT
		}
	}

	for _, n := range nums {
		n = abs(n)
		if n < 1 || n > len(nums) {
			continue
		}
		i := abs(n) - 1
		if nums[i] > 0 {
			nums[i] = -nums[i]
		}
	}

	for i, n := range nums {
		if n >= 0 {
			return i + 1
		}
	}

	return len(nums) + 1
}

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func main() {
	fmt.Println(firstMissingPositive([]int{1, 2, 0}))
	fmt.Println(firstMissingPositive([]int{3, 4, -1, 1}))
	fmt.Println(firstMissingPositive([]int{0, 1, 2}))
}
