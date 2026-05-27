# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start = head
        middle = self.findMiddleNode(head)
        print(middle.val)
        end = self.reverseList(middle.next)
        middle.next = None
        while end:
            temp1, temp2 = start.next, end.next
            start.next = end
            end.next = temp1
            start,end = temp1,temp2
    
    def findMiddleNode(self, head: Optional[ListNode]) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev