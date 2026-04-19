# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        ll1 = []
        ll2 = []
#make 2 lists out of the Linked lists
        while(curr1):
            ll1.append(curr1.val)
            curr1 = curr1.next
           
        while(curr2):
            ll2.append(curr2.val)
            curr2 = curr2.next
#make lists equal sizes
        n = max(len(ll1), len(ll2))
        while len(ll1) < n:
            ll1.append(0)
        while len(ll2) < n:
            ll2.append(0)

#add them, account for carry
        res = []
        carry = 0
        for i in range(len(ll1)):
            total = ll1[i] + ll2[i] + carry
            carry = total // 10
            digit = total % 10

            res.append(digit)

        if(carry):
            res.append(carry)
        dummy = ListNode(0)
        tail = dummy

        for num in res:
            tail.next = ListNode(num)
            tail = tail.next

        return dummy.next