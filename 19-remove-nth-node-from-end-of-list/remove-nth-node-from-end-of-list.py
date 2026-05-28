from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        # Advance fast pointer so there is a gap of n nodes between slow and fast
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers together until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
            
        # slow is now right before the node to be removed
        slow.next = slow.next.next
        
        return dummy.next
