__author__ = "kenzhaoyihui"

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        tmp = x
        y = 0
        while tmp:
            y = y*10 + tmp%10
            tmp = tmp/10
        return y == x

if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome(-1)
    print s.isPalindrome(12)
    print s.isPalindrome(121)