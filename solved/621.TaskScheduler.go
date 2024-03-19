package main

import "fmt"

func leastInterval(tasks []byte, n int) int {
	if n == 0 {
		return len(tasks)
	}

	remaining := make([]int, 26)
	for _, t := range tasks {
		remaining[t-'A'] += 1
	}

	max_frequency := -1
	number_of_maxes := 0
	for _, r := range remaining {
		if r > max_frequency {
			number_of_maxes = 1
			max_frequency = r
		} else if r == max_frequency {
			number_of_maxes++
		}
	}

	gap := n - (number_of_maxes-1)
	gaps := gap * (max_frequency-1)

	// not enough gaps
	if len(tasks) - (number_of_maxes*max_frequency) > gaps {
		return len(tasks)
	} else { // enough gaps
		return gaps + (number_of_maxes * max_frequency)
	}
}

func main() {
	fmt.Println(leastInterval([]byte{'A', 'A', 'A', 'B', 'B', 'B'}, 2))
	fmt.Println(leastInterval([]byte{'A', 'C', 'A', 'B', 'D', 'B'}, 1))
	fmt.Println(leastInterval([]byte{'A', 'A', 'A', 'B', 'B', 'B'}, 3))
}
