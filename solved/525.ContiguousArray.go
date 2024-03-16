package main

import "fmt"

func findMaxLength(nums []int) int {
	found := make(map[int]int)
	res := 0

	sum := 0
	found[0] = 0

	for i, n := range nums {
		if n == 0 {
			sum -= 1
		} else {
			sum += 1
		}

		if val, ok := found[sum]; ok {
			res = max(res, i-val+1)
		} else {
			found[sum] = i + 1
		}
	}

	return res
}

func main() {
	fmt.Println(findMaxLength([]int{0, 1, 0}))
	fmt.Println(findMaxLength([]int{0, 1}))
}
