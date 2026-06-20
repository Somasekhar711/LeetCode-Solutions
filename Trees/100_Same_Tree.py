# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        else:
            if p.val==q.val:
                return ( self.isSameTree(p.left,q.left) and
                self.isSameTree(p.right,q.right) )
                return True
            else:
                return False

# Approach: Recursive Tree Comparison
# Time Complexity: O(min(m, n)) - Visit each node of smaller tree
# Space Complexity: O(min(h1, h2)) - Call stack depth, limited by shorter tree height
