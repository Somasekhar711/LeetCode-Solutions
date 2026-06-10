class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)

        if n <= 1:
            return s

        start = 0
        end = 0
        plen = 1

        for i in range(n):

            left = i
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > plen:
                    plen = right - left + 1
                    start = left
                    end = right

                left -= 1
                right += 1

            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > plen:
                    plen = right - left + 1
                    start = left
                    end = right

                left -= 1
                right += 1

        return s[start:end + 1]