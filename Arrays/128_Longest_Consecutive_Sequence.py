class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        num_set = set(nums)
        best = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                best = max(best, length)

        return best


# Approach: Use a hash set and only start counting from the leftmost value of each consecutive run.
# Time Complexity: O(n) average time because each number is processed a constant number of times.
# Space Complexity: O(n) for the set of numbers.
