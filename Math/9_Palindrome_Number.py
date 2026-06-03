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