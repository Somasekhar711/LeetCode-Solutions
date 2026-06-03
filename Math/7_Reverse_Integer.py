class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rx = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            rx = (rx * 10) + (x % 10)
            x //= 10

        rx *= sign

        if rx < -2147483648 or rx > 2147483647:
            return 0

        return rx
        