class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        top = -1

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stk.append(c)
                top += 1
            else:
                if top == -1:
                    return False

                p = stk[top]

                if ((c == ')' and p == '(') or
                    (c == ']' and p == '[') or
                    (c == '}' and p == '{')):
                    stk.pop()
                    top -= 1
                else:
                    return False

        if top == -1:
            return True
        else:
            return False