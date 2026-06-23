class Solution(object):
    def climbStairs(self, n):
        ways=[0]*(n+1)
        ways[n]=1
        i=n-1
        while i>=0 :
            ways[i]=0
            if i+1<=n:
                ways[i]+=ways[i+1]
            if i+2<=n:
                ways[i]+=ways[i+2]
            i-=1
        return ways[0]

# Approach: Bottom-Up Dynamic Programming
# Time Complexity: O(n) - Single pass to build dp array
# Space Complexity: O(n) - dp array of size n+1