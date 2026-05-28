# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Dummy node acts as a temporary anchor for the merged list head
        dummy = ListNode(-1)
        current = dummy
        
        # Traverse both lists until one runs out of nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # Append the remaining nodes from whichever list is not empty
        current.next = list1 if list1 else list2
        
        # The real head is the node immediately following the dummy node
        return dummy.next
