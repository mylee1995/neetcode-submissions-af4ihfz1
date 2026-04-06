# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        curr = dummyNode
        trailing = 0
        while l1 or l2:
            l1Val = l1.val if l1 is not None else 0
            l2Val = l2.val if l2 is not None else 0
            val = l1Val + l2Val + trailing
            if val > 9:
                trailing = 1
                val = val - 10
            else:
                trailing = 0
            
            newNode = ListNode(val)
            curr.next = newNode
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if trailing > 0:
            curr.next = ListNode(trailing)

        return dummyNode.next
