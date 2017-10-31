__author__ = "kenzhaoyihui"

class Solution(object):
    """
    1. x=123454321, y=0             |       1. x=12344321, y=0
    2. x=12345432, y=1              |       2. x=1234432, y=1
    3. x=1234543, y=12              |       3. x=123443, y=12
    4. x=123454, y=123              |       4. x=12344, y=123
    5. x=12345, y=1234              |       5. x=1234, y=1234 (y==x)
    6. x=1234, y=12345  (y/10=x)    |
    """
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 ==0):
            return False

        y = 0
        while y<x:
            y = y*10 + x%10
            x = x/10
        return y == x or y/10 == x

if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome(-1)
    print s.isPalindrome(1000)
    print s.isPalindrome(121)
    print s.isPalindrome(123454321) 