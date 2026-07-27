# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=[root.val]

        def dfs(root):
            if not root:
                return 0
            lm=dfs(root.left)
            rm=dfs(root.right)
            lm=max(lm,0)
            rm=max(rm,0)

            res[0]=max(res[0],root.val+lm+rm)

            return root.val+max(lm,rm)
        dfs(root)
        return res[0]


# Approach: DFS returns the maximum contribution from each subtree, while tracking the maximum path sum through each node.
# Time Complexity: O(n) — each node is visited once.
# Space Complexity: O(h) recursion stack, where h is the tree height.