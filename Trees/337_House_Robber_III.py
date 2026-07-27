# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(root):
            if not root:
                return [0,0]
            
            lp=dfs(root.left)
            rp=dfs(root.right)

            ir = root.val+lp[1]+rp[1]
            er = max(lp)+max(rp)

            return [ir,er]
        return max(dfs(root))


# Approach: Use DFS to compute two values per node: max rob amount including the node and max rob amount excluding it.
# Time Complexity: O(n) — each node is visited once.
# Space Complexity: O(h) recursion stack, where h is the tree height.
