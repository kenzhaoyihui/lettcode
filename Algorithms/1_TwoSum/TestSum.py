# /usr/bin/env python2.7
"""
a = raw_input()
b = []
c = []
b = list(a)


for i in range(0,len(b)):
    c.append(b[i])


if b[0] == b[len(b)-1]:
    for i in range(1,len(b)):
        c.append(b[i])
print "".join(c)
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        for i in range(len(nums)):
            for k in range(len(nums)):
                if nums[i] + nums[k] == target:
                    return [i,k]
        """
        """
        process = {}
        for index in range(len(nums)):
            if target-nums[index] in process:
                return [process[target-nums[index]],index]
            process[nums[index]]=index
        """
        
        if len(nums) <= 1:
            return False
        b_dict = {}
        for i in range(len(nums)):
            if nums[i] in b_dict:
                return [b_dict[nums[i]], i]
            else:
                b_dict[target-nums[i]] = i
        

if __name__ == "__main__":
    f = Solution()
    print f.twoSum([2,7,11,13], 15)