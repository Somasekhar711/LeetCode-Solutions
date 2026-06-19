# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev=None
        current=head
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        head=prev
        return head

# Approach: Iterative Reversal (Three Pointers)
# Time Complexity: O(n) - Single pass through the list
# Space Complexity: O(1) - Only using three pointer variables