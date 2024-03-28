package main

func maxSubarrayLength(nums []int, k int) int {
	freqs := make(map[int]int)
	start, res := 0, 0

	for end := 0; end < len(nums); end++ {
		freqs[nums[end]]++
		for freqs[nums[end]] > k {
			freqs[nums[start]]--
			start++
		}

		res = max(res, end-start+1)
	}
	return res
}
