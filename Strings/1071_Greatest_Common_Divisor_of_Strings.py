# LeetCode 1071: Greatest Common Divisor of Strings
# Approach: Test the largest possible prefix length that divides both strings exactly.
# Time Complexity: O(n * m) in the worst case for repeated string comparisons
# Space Complexity: O(1)

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1=len(str1)
        len2=len(str2)

        def isDivisor(l):
            if len1%l or len2%l:
                return False
            f1=len1//l
            f2=len2//l
            return str1[:l]*f1==str1 and str1[:l]*f2==str2
        
        for l in range(min(len1,len2),0,-1):
            if isDivisor(l):
                return str1[:l]
        return ""
        