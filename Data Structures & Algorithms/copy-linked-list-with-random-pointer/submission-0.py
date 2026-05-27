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
        old_to_new = {None: None}

        def get_or_create(node):
            if node not in old_to_new:
                old_to_new[node] = Node(node.val)
            return old_to_new[node]
        
        curr = head
        while curr:
            copy = get_or_create(curr)
            copy.next = get_or_create(curr.next)
            copy.random = get_or_create(curr.random)
            curr = curr.next
        
        return old_to_new[head]
        
        