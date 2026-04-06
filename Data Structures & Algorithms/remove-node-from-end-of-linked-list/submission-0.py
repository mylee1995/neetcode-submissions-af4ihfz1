# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr: 
            size += 1
            curr = curr.next

        
        # size is 4, n = 2
        curr = head
        counter = 0
        prev = None
        while counter < size - n:
            counter += 1
            prev = curr
            curr = curr.next

        if prev == None:
            return curr.next
        
        
        print(prev.val)
        prev.next = curr.next

        return head