class Solution(object):
    def maxArea(self, height):
        max_val = 0
        temp = 0
        right = len(height) - 1
        left = 0

        while left < right:
            temp = min(height[left], height[right]) * (right - left)

            if temp > max_val:
                max_val = temp

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_val

# Approach: Two Pointers (Greedy)
# Time Complexity: O(n) - Single pass with two pointers moving inward
# Space Complexity: O(1) - Only using constant extra space