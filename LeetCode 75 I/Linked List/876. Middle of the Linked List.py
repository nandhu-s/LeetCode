# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        h=head
        c=0
        while t:
            c=c+1
            t=t.next
        if c%2==0:
            n=(c/2)+1
        else:
            n=ceil(c/2)
        for i in range(1,int(n)):
            h=h.next
        return (h)
