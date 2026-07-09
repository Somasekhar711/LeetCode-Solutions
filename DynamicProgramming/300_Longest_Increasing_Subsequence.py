class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    dp[i]=max(dp[i],1+dp[j])
        return max(dp)


# Approach: Use backward DP to compute the length of the longest increasing subsequence ending at each position.
# Time Complexity: O(n^2) due to nested loops comparing all pairs of elements.
# Space Complexity: O(n) for the DP array.

