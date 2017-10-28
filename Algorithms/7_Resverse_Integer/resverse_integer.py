# -*-coding: utf-8 -*-
__author__ = "kenzhaoyihui"

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if 0<x<2147483647:
            xx = str(x)
            xxx = int(xx[::-1])
            if xxx>=2147483647:
                return 0
        elif -2147483648<x<0:
            xx = str(abs(x))
            xxx = -int(xx[::-1])
            if xxx<=-2147483648:
                return 0
        else:
             return 0    
        return xxx
        """
        isNegative = x < 0
        if isNegative:
            x=-x
        rtn = 0;
        max32 = 2**31-1  # 32位符号整数的最大值
        while x != 0:
            postBit = x%10
            iterval = rtn*10 + postBit
            if iterval > max32:
                return 0
            rtn = iterval
            x /= 10
        return -rtn if isNegative else rtn 
        """
if __name__ == "__main__":
    s = Solution()
    print s.reverse(12367)
    print s.reverse(-12367)
