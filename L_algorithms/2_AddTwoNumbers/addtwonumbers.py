# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        number1 = 0
        number2 = 0
        power = 0
        while l1 and l2:
            number1 += l1.val*10**power
            l1 = l1.next
            number2 += l2.val*10**power
            l2 = l2.next
            power += 1
            
        summed = number1 + number2
        listSummed = list(str(summed))
        #listSummed = list(reversed(listSummed)) if they wanted the solution reversed
        
        head = ListNode(listSummed[0])
        for ind in range(1, len(listSummed)):
            n = ListNode(listSummed[ind])
            n.next = head
            head = n
        
        return head
        
    """ 
        resultNode = None
        add = 0
        while True:
            if l1.val == -1:
                l1.val = 0
            if l2.val == -1:
                l2.val = 0

            tsum = (l1.val + l2.val + add) % 10
            add = (l1.val + l2.val +add) / 10
            listn = ListNode(tsum)

            if resultNode == None:
                resultNode = listn
                flagNode = resultNode
            else:
                flagNode.next = listn
                flagNode = flagNode.next

            if l1.next != None:
                l1 = l1.next
            else:
                l1.val = -1

            if l2.next != None:
                l2 = l2.next
            else:
                l2.val = -1

            if l1.val == -1 and l2.val == -1:
                break

        if add != 0:
            listn = ListNode(add)
            flagNode.next = listn

        return resultNode
    """
if __name__ == '__main__':
    l1_1 = ListNode(2)
    l1_1.next = ListNode(4)
    l1_1.next.next = ListNode(3)

    l2_1 = ListNode(5)
    l2_1.next = ListNode(6)
    l2_1.next.next = ListNode(4)

    s = Solution()
    res = s.addTwoNumbers(l1_1, l2_1)
    print "{0} -> {1} -> {2}".format(res.val, res.next.val , res.next.next.val)
