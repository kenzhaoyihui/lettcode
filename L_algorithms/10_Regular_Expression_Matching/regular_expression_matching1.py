__author__ = "kenzhaoyihui"

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)==0:
            return len(s)==0
        if len(p)==1 or p[1]!='*':
            if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatch(s[1:], p[1:])
        else:
            i=-1
            length = len(s)
            while i<length and (i<0 or p[0]=='.' or p[0]==s[i]):
                if self.isMatch(s[i+1:], p[2:]):
                    return True
                i += 1
            return False

if __name__ == "__main__":
    s = Solution()
    print s.isMatch("aa","a")
    print s.isMatch("aa","aa")
    print s.isMatch("aaa","aa")
    print s.isMatch("aa", "a*")
    print s.isMatch("aa", ".*")
    print s.isMatch("ab", ".*")
    print s.isMatch("aab", "c*a*b")
    print s.isMatch("abcd", "d*")
    print s.isMatch("aa", ".")
    print s.isMatch("a", ".")
    print s.isMatch("", "")
    print s.isMatch("abcd", "")
