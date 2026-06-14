class Solution(object):
    def isPalindrome(self, s):
        st=""
        for c in s:
            if c.isalnum() :
                st+=c.lower()
        n=len(st)
        start=0
        end=n-1
        while start<=end :
            if st[start]==st[end]:
                start+=1
                end-=1
            else:
                return False
        return True        