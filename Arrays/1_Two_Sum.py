class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i,num in enumerate(nums) :
            complement=target-num
            if complement in seen :
                return[seen[complement],i]
            seen[num]=i
        return[]

# Approach: Hash Map (Single Pass)
# Time Complexity: O(n) - Single pass through the array
# Space Complexity: O(n) - Hash map stores up to n elements