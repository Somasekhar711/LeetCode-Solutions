# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res=0
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)

            self.res=max(self.res,left+right)
            return 1+(max(left,right))
        dfs(root)    
        return self.res


    # Approach: Post-order DFS that computes the height of each subtree; at each node update the maximum diameter seen as left_height + right_height.
    # Time Complexity: O(n) — each node is visited once.
    # Space Complexity: O(h) recursion stack where h is the tree height.