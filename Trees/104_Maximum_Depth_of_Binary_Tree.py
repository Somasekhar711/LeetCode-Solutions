# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return 1 + max(
                self.maxDepth(root.left),
                self.maxDepth(root.right)
            )

# Approach: Recursive DFS
# Time Complexity: O(n) - Visit each node once
# Space Complexity: O(h) - Call stack depth, h = tree height (O(n) worst case for skewed tree)