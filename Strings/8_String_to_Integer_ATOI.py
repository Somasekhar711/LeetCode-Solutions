class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = False
        i = 0
        q = False
        idx = 0

        while idx < len(s):
            temp = ord(s[idx])

            if (s[idx] == ' ' or s[idx] == '\t') and q == False:
                idx += 1
                continue

            elif s[idx] == '+' and q == False:
                q = True
                idx += 1

            elif s[idx] == '-' and q == False:
                k = True
                q = True
                idx += 1

            elif 0 <= temp - 48 < 10:

                if i > (2147483647 // 10) or (
                    i == 2147483647 // 10 and temp - 48 > 7
                ):
                    return -2147483648 if k else 2147483647

                i = (i * 10) + (temp - 48)
                idx += 1
                q = True

            else:
                break

        if k:
            i = -i

        if i > 2147483647:
            i = 2147483647
        elif i < -2147483648:
            i = -2147483648

        return i

# Approach: State Machine with Input Validation
# Time Complexity: O(n) - Single pass through input string
# Space Complexity: O(1) - Only using constant extra space for variables