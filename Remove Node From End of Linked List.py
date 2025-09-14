# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow,fast=head,head 
        prev=None
        while n:
            fast=fast.next
            n-=1
        
        while fast:
            prev=slow
            slow=slow.next
            fast=fast.next


        if slow==head: return head.next
        if prev: prev.next=slow.next

        return head
        # TC:O(N)
        #SC:O(1)


        
