__author__ = "kenzhaoyihui"

class Solution(object):
    def maxArea(self, height):
        size = len(height)
        maxm = 0
        for i in range(size):
            for k in range(size):
                if height[i]<=height[k]:
                    maxm = max(maxm, height[i]*abs(k-i))
                else:
                    maxm = max(maxm, height[k]*abs(k-i))
        return maxm

if __name__ == "__main__":
    s = Solution()
    print s.maxArea([1,3,5,9,2,4,7])
    print s.maxArea([9,8,7,1,2,3,9,8,3])
