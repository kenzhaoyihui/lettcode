//package main
package kenzhaoyihui

import (
	"fmt"
	"sort"
)

func twoSum(nums []int, target int) []int {
	indexs := make([]int, 2)
	hash := make(map[int]int)
	error := []int{0, 0}

	if len(nums) <= 1 {
		fmt.Println("Error!")
		return error
	}

	for i := range nums {
		hash[target-nums[i]] = i
	}

	for i := range nums {
		index, ok := hash[nums[i]] // 查看集合中元素是否存在
		if ok {
			if i == index {
				continue
			}
			indexs[0] = i
			indexs[1] = index
			sort.Ints(indexs)
			break
		}
		continue
	}
	return indexs
}

/*
func main() {
	list := []int{2, 3, 4, 6}
	value := 6
	fmt.Println(twoSum(list, value))

}
*/