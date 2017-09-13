package kenzhaoyihui

import "testing"
import "fmt"

func TestTwoSum(t *testing.T) {
	if result := twoSum([]int{1, 2, 3, 4}, 7); result[0] != 2 && result[1] != 3 {
		t.Errorf("Error")
	}

	if result1 := twoSum([]int{2, 3, 4, 5}, 9); result1[0] == 2 && result1[1] == 3 {
		fmt.Println("Successfilly!")
	}
}
