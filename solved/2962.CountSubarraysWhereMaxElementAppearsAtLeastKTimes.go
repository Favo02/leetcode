package main

import (
	"fmt"
	"slices"
)

func countSubarrays(nums []int, k int) int64 {
	MAX := slices.Max(nums)
	res := int64(0)

	start, count := 0, 0
	for end := 0; end < len(nums); end++ {
		if nums[end] == MAX {
			count++
		}
		// remove extra elements before first MAX
		for start < len(nums) && nums[start] != MAX {
			if nums[start] == MAX {
				count--
			}
			start++
		}
		if count == k {
			after := 0
			for _, n := range nums[end+1:] {
				if n == MAX {
					break
				}
				after++
			}
			res += int64(1 + start + after + (start * after))

			// force window slide
			start++
			count--
		}
	}

	return res
}

func main() {
	fmt.Println(countSubarrays([]int{1, 3, 2, 3, 3}, 2))
	fmt.Println(countSubarrays([]int{1, 3, 2, 3, 3, 1, 3}, 2))
	fmt.Println(countSubarrays([]int{1, 4, 2, 1}, 3))
	fmt.Println(countSubarrays([]int{61, 23, 38, 23, 56, 40, 82, 56, 82, 82, 82, 70, 8, 69, 8, 7, 19, 14, 58, 42, 82, 10, 82, 78, 15, 82}, 2))
	fmt.Println(countSubarrays([]int{28,5,58,91,24,91,53,9,48,85,16,70,91,91,47,91,61,4,54,61,49}, 1))
}
