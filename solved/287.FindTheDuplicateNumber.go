package main

func findDuplicate(nums []int) int {
	s, f := nums[0], nums[0]
	for {
		s = nums[s]
		f = nums[f]
		f = nums[f]
		if s == f {
			break
		}
	}

	s = nums[0]
	for {
		if s == f {
			return s
		}
		s = nums[s]
		f = nums[f]
	}
}
