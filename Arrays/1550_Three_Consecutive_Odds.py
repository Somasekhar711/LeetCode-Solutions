class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i = 0
        count = 0

        while i < len(arr) - 2:
            for j in range(i, i + 3):
                if (arr[j] % 2) == 1:
                    count += 1

            if count == 3:
                return True
            else:
                count = 0
                i += 1

        return False

# Approach: Sliding Window with Counter
# Time Complexity: O(n^2) - Nested loops for checking windows
# Space Complexity: O(1) - Only using a counter variable