package main

import (
	"fmt"
)

func main() {
	x := 12367
	y := -12367
	fmt.Println(reverse(x), reverse(y))
}

func reverse(x int) int {
	sum := 0
	for {
		left := x / 10
		last := x % 10
		x = left
		sum = sum*10 + last

		if left == 0 {
			break
		}
	}

	if sum <= -2147483648 || sum >= 2147483648 {
		sum = 0
	}
	return sum
}
