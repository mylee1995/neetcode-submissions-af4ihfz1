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
        nodeMap = {None: None}

        dummyNode = Node(0)
        copyPointer = dummyNode

        curr = head
        while curr:
            newNode = Node(curr.val)
            nodeMap[curr] = newNode

            copyPointer.next = newNode
            copyPointer = copyPointer.next
            curr = curr.next
        

        copyPointer = dummyNode.next
        curr = head
        while curr and copyPointer:
            copyPointer.random = nodeMap[curr.random]
            curr = curr.next
            copyPointer = copyPointer.next


        return dummyNode.next
