package main

func findDuplicates(nums []int) []int {
	res := make([]int, 0)
	for _, n := range nums {
		n = abs(n)
		if nums[n-1] < 0 {
			res = append(res, n)
		} else {
			nums[n-1] = -nums[n-1]
		}
	}
	return res
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
