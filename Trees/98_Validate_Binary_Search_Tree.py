# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):

        def validate(root, low, high):
            if not root:
                return True

            if root.val <= low or root.val >= high:
                return False

            return (validate(root.left, low, root.val) and
                    validate(root.right, root.val, high))

        return validate(root, float('-inf'), float('inf'))

# Approach: Recursive DFS with bounds
# Time Complexity: O(n) - Visit each node once
# Space Complexity: O(h) - Recursion stack depth, h = tree height