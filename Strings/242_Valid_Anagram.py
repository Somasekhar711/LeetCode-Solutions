class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        for c in t:
            if c not in count:
                return False

            count[c] -= 1

            if count[c] < 0:
                return False

        return True

# Approach: Hash Map Frequency Counting
# Time Complexity: O(n) - Two passes through strings, s first then t
# Space Complexity: O(1) - Hash map stores at most 26 characters (alphabet)