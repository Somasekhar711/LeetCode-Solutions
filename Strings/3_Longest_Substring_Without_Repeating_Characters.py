class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hs = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):
            while s[right] in hs:
                hs.remove(s[left])
                left += 1

            hs.add(s[right])

            currentLen = right - left + 1
            if currentLen > maxLen:
                maxLen = currentLen

        return maxLen

# Approach: Sliding Window with Set
# Time Complexity: O(n) - Each character visited at most twice (left and right pointers)
# Space Complexity: O(min(n, 26)) - Set stores at most 26 unique characters (ASCII alphabet)