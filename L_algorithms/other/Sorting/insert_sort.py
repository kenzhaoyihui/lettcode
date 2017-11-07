#-*- coding: utf-8 -*-
__author__ = "kenzhaoyihui"

def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

if __name__ == "__main__":
    list1 = [9,8,7,6,5,4,3,2,1]
    list2 = [1,3,2,6,4,7,9,2,4]

    print insert_sort(list1)
    print insert_sort(list2)
