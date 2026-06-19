class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        temp = 1
        digit1 = 0
        digit2 = 0
        while l1.next :
            digit1 = digit1 + ( l1.val * temp )
            l1 = l1.next
            temp = temp * 10

        digit1 = digit1 + ( l1.val * temp )

        temp = 1
        
        while l2.next :
            digit2 = digit2 + ( l2.val * temp )
            l2 = l2.next
            temp = temp * 10
        
        digit2 = digit2 + ( l2.val * temp )
        ans = digit1 + digit2
        answer = ListNode(0)
        current = answer

        current.next = ListNode( ans % 10 )
        current = current.next
        ans = ans / 10
        
        while ans :
            current.next = ListNode( ans % 10 )
            current = current.next
            ans = ans / 10
        return answer.next

# Approach: Convert to integers, add, convert back to linked list
# Time Complexity: O(m + n) - Traverse both lists to convert, then add
# Space Complexity: O(max(m, n)) - Result list has maximum length


        
        