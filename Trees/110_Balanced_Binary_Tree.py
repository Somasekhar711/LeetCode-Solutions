# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            is_balanced = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)
            return [is_balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


# Approach: Post-order DFS that returns whether the subtree is balanced and its height.
# Time Complexity: O(n) because each node is visited once.
# Space Complexity: O(h) for the recursion stack, where h is the tree height.
