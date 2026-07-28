class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w))<=len(s) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]


# Approach: Bottom-up DP over string positions; dp[i] is True if s[i:] can be segmented using dictionary words.
# Time Complexity: O(n * m * k) in the worst case, where n = len(s), m = number of words, and k = average word length.
# Space Complexity: O(n) for the DP array.