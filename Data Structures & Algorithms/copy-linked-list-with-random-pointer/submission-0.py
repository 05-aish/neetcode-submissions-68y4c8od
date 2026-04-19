"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hmap = {None : None}
#copying nodes and putting it in hmap
        while(curr):
            copy = Node(curr.val)
            hmap[curr] = copy
            curr = curr.next
#assign pointers
        curr = head
        while(curr):
            copy = hmap[curr]
            copy.next = hmap[curr.next]
            copy.random = hmap[curr.random]
            curr = curr.next
        return hmap[head]