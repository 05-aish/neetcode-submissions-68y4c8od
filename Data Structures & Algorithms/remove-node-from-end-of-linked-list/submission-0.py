# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(head == None):
                return
        l = head
        count = 0
#length of list
        while(l != None):
                count += 1
                l = l.next

#one pass soln
        dummy = ListNode(0, head)
        first = dummy
        for i in range(n + 1):
                first = first.next
        second = dummy
        while(first):
                first = first.next
                second = second.next
        second.next = second.next.next
        return dummy.next

