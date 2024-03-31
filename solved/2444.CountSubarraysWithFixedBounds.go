package main

import "fmt"

func countSubarrays(nums []int, minK int, maxK int) int64 {
	res := int64(0)

	start := 0
	mi, ma := -1, -1
	for end, n := range nums {
		if n < minK || n > maxK {
			start = end + 1
		}

		if n == minK {
			mi = end
		}
		if n == maxK {
			ma = end
		}

		if mi >= start && ma >= start {
			res += int64(1 + min(mi, ma) - start)
		}
	}

	fmt.Println(res)
	return res
}

func main() {
	countSubarrays([]int{1, 3, 2, 4, 1, 5, 2, 7, 7, 5}, 1, 5)
	countSubarrays([]int{1, 1, 1, 1}, 1, 1)
	countSubarrays([]int{1, 3, 2, 1, 4, 1, 5, 2, 7, 1, 5, 8}, 1, 5)
	countSubarrays([]int{35054, 398719, 945315, 945315, 820417, 945315, 35054, 945315, 171832, 945315, 35054, 109750, 790964, 441974, 552913}, 35054, 945315)
	countSubarrays([]int{35, 398, 945, 945, 820, 945, 35, 945, 171, 945, 35, 109, 790, 441, 552}, 35, 945)
}
