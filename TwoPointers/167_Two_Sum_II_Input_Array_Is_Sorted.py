class Solution(object):
    def twoSum(self, numbers, target):
        ans=[]
        size=len(numbers)
        low=0
        high=size-1
        while low<high :
            current=numbers[high]+numbers[low]
            if current==target:
                ans.append(low+1)
                ans.append(high+1)
                return ans
            elif current<target:
                low+=1
            elif current>target:
                high-=1
        return ans