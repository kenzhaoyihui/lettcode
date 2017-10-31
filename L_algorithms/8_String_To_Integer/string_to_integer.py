__author__ = "kenzhaoyihui"

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        base = 0
        flag = 1
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        l = len(str)

        while i<l and str[i] == ' ':
            i += 1
        if i<l and str[i] == '-':
            flag = -1
            i += 1
        elif i<l and str[i] == '+':
            i += 1
        
        while i <l and ord(str[i])>=48 and ord(str[i])<=57:
            if base > INT_MAX/10 or (base == INT_MAX/10 and ord(str[i])-48>7):
                return flag == 1 and INT_MAX or INT_MIN
            base = 10 * base + ord(str[i])-48
            i += 1
        return base * flag

if __name__ == "__main__":
    s = Solution()
    print s.myAtoi("     -123456")
    print s.myAtoi("   -")
    print s.myAtoi("     ++123")
    print s.myAtoi("0123456")
    print s.myAtoi("+0123456")
    print s.myAtoi("+++12345")
    print s.myAtoi("-0123456")
    print s.myAtoi("01234567890000")
    print s.myAtoi("-03y443yu329883874242")
    print s.myAtoi("-1234567890000000")
