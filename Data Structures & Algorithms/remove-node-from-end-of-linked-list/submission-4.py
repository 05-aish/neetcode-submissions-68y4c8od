# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(head == None):
                return None
        arr = []
        count = 0
        l = head
        while(l):
                arr.append(l.val)
                count += 1
                l = l.next
        idx = count - n
        arr.pop(idx)
        dummy = ListNode()
        tail = dummy
        for i in arr:
                tail.next = ListNode(i)
                tail = tail.next

        return dummy.next