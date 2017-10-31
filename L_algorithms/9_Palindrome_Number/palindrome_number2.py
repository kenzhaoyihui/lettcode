__author__ = "kenzhaoyihui"

class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False

        xx = list(str(x))
        for i in range(len(str(x))):
            if xx[i] != xx[::-1][i]:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome(-1)
    print s.isPalindrome(12)
    print s.isPalindrome(121)





