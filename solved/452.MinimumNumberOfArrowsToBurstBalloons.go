package main

import (
	"fmt"
	"sort"
)

func findMinArrowShots(points [][]int) int {
	sort.Slice(points, func(i, j int) bool {
		return points[i][0] < points[j][0]
	})

	res := 1

	minn := points[0][0]
	maxx := points[0][1]

	for i := 0; i < len(points); i++ {
		if points[i][0] > maxx { // stop accumulating
			minn = points[i][0]
			maxx = points[i][1]
			res += 1
		} else { // accumulate
			minn = max(minn, points[i][0])
			maxx = min(maxx, points[i][1])
		}
	}

	return res
}

func main() {
	fmt.Println(findMinArrowShots([][]int{{10, 16}, {2, 8}, {1, 6}, {7, 12}}))
	fmt.Println(findMinArrowShots([][]int{{1, 2}, {3, 4}, {5, 6}, {7, 8}}))
}
