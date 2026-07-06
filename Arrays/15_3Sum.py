class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        ans=[]
        triplet=[]
        for i,num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target=0-num
            triplets=self.twoSum(nums[i+1:n],target,num)
            if triplets:
                ans.extend(triplets)
        return ans


    def twoSum(self,nums, target,fnum):
        seen={}
        results=[]
        for i,num in enumerate(nums) :
            complement=target-num
            if complement in seen :
                triplet=[fnum,complement,num]
                if triplet not in results:
                    results.append(triplet)
            seen[num]=i
        return results


# Approach: Sort the array then use a two-pointer scan per fixed first element to find unique triplets summing to zero.
# Time Complexity: O(n^2) due to nested scanning after sort.
# Space Complexity: O(n) for the result storage and seen map.
