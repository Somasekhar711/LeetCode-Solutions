# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if not root:
            return root
        else:
            temp=root.left
            root.left=root.right
            root.right=temp
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            return root
        
# Approach: Recursive Tree Traversal with Node Swap
# Time Complexity: O(n) - Visit each node once to swap children
# Space Complexity: O(h) - Call stack depth, h = tree height (O(n) worst case for skewed tree)