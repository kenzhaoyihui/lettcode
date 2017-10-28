__Author__ = "kenzhaoyihui"


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = []
        for i in nums1:
            num.append(i)
        for k in nums2:
            num.append(k)

        new_num = sorted(num)
        count = len(new_num)

        if count%2 == 0:
            return (new_num[count/2 - 1] + new_num[count/2])/2.0
        else:
            return new_num[count/2]

if __name__ == "__main__":
    nums1 = [1,4,3,2,5,7]
    nums2 = [1,2,3,4,5]
    s = Solution()
    print s.findMedianSortedArrays(nums1, nums2)
        