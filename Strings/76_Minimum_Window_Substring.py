class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t=="":
            return ""
        
        count,window={},{}
        for c in t:
            count[c]=1+count.get(c,0)
        have=0
        need=len(count)
        res=[-1,-1]
        resLen=float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in count and window[c]==count[c]:
                have+=1
            while have==need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=(r-l+1)
                window[s[l]]-=1
                if s[l] in count and window[s[l]]<count[s[l]]:
                    have-=1
                l+=1
        l,r=res
        if resLen!=float("infinity"):
            return s[l:r+1]
        else:
            return ""


# Approach: Sliding window with two hash maps. Expand the right boundary to satisfy required characters, then shrink from the left to find the minimum valid window.
# Time Complexity: O(n + m) where n = len(s) and m = len(t), because each character enters/leaves the window at most once.
# Space Complexity: O(k) for the count maps, where k is the number of unique characters in t.
