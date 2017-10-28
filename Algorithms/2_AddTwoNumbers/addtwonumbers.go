/**
 * Definition for singly-linked list.
 */

//Have the problem about the main function
/*
package main

import "fmt"

func main() {
	var d1 *ListNode
	var d2 *ListNode

	d1.Val = 1
	d1.Next.Val = 4
	d1.Next.Next.Val = 3

	d2.Val = 2
	d2.Next.Val = 4
    d2.Next.Next.Val = 6
*/
/*
	for i := 0; i < 3; i++ {
		d1.Val = i
	}
	for i := 6; i < 9; i++ {
		d2.Val = i
	}
*/

//fmt.Println(d1)
//fmt.Println(d2)

//result := addTwoNumbers(d1, d2)
//fmt.Println(result.Val, result.Next.Val, result.Next.Next.Val)
//}

package kenzhaoyihui

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	l3 := &ListNode{}
	L3 := l3
	carry := 0

	for l1 != nil || l2 != nil || carry > 0 {

		sum := carry

		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}

		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}

		L3.Next = &ListNode{}
		L3.Next.Val = sum % 10
		carry = sum / 10
		L3 = L3.Next
	}
	return l3.Next
}
