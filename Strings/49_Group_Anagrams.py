class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []

        strs.sort(key=len)

        grp = []
        visited = [False] * len(strs)
        i = 0

        while i < len(strs):

            if visited[i]:
                i += 1
                continue

            anagram = [strs[i]]
            visited[i] = True

            count = {}
            for c in strs[i]:
                count[c] = count.get(c, 0) + 1

            j = i + 1

            while j < len(strs) and len(strs[j]) == len(strs[i]):

                if visited[j]:
                    j += 1
                    continue

                dup_count = count.copy()
                match = True

                for c in strs[j]:
                    if c not in dup_count:
                        match = False
                        break

                    dup_count[c] -= 1
                    if dup_count[c] < 0:
                        match = False
                        break

                if match and all(v == 0 for v in dup_count.values()):
                    anagram.append(strs[j])
                    visited[j] = True

                j += 1

            grp.append(anagram)
            i += 1

        return grp


# Approach: Group strings by character frequency while keeping only same-length candidates to reduce comparisons.
# Time Complexity: O(n * m * k) in the worst case, where n is number of strings, m is average string length, and k is the number of same-length comparisons.
# Space Complexity: O(n * m) for the grouped result and temporary frequency maps.
