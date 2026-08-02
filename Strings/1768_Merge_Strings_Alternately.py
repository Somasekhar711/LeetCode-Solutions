# LeetCode 1768: Merge Strings Alternately
# Approach: Use two pointers and append characters alternately from each string.
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        merged = []

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged.append(word1[i])
                i += 1
            if j < len(word2):
                merged.append(word2[j])
                j += 1

        return "".join(merged)


if __name__ == "__main__":
    print(Solution().mergeAlternately("abc", "pqr"))  # Expected: apbqcr
    print(Solution().mergeAlternately("ab", "pqrs"))  # Expected: apbqrs
    print(Solution().mergeAlternately("abcd", "pq"))  # Expected: apbqcd
        