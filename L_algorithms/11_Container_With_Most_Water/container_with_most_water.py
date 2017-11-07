__author__ = "kenzhaoyihui"

class Solution(object):
    def maxArea(self, height):
        """
        :type: height: List[int]
        :rtype: int
        """

        size = len(height)
        maxm = 0
        j = 0
        k = size - 1

        while j<k:
            if height[j]<=height[k]:
                maxm = max(maxm, height[j]*(k-j))
                j += 1
            else:
                maxm = max(maxm, height[k]*(k-j))
                k -= 1
        return maxm

if __name__ == "__main__":
    s = Solution()
    print s.maxArea([1,3,5,9,2,4,7])
    print s.maxArea([9,8,7,1,2,3,9,8,3])
