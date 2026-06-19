class Solution(object):
    def isPalindrome(self, x):
        if x == 0:
            return True

        if x < 0:
            return False

        rx = 0
        temp = x

        while temp != 0:
            rx = rx * 10 + temp % 10
            temp //= 10

        return rx == x

# Approach: Extract digits and reverse, then compare
# Time Complexity: O(log x) - Number of digits in x
# Space Complexity: O(1) - Only using constant extra space