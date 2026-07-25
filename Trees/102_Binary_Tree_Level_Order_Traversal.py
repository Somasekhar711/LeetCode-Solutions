from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[]
        cln=1
        q=deque()
        q.append(root)
        nodes=[]
        while q:
            top=q.popleft()
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
            cln-=1
            nodes.append(top.val)
            if cln==0:
                res.append(nodes)
                nodes=[]
                cln=len(q)
        return res


# Approach: Breadth-first search using a queue (`collections.deque`) to collect node values level-by-level. Track current level size to group values per level.
# Time Complexity: O(n) — each node is visited once.
# Space Complexity: O(w) where w is the maximum width of the tree (queue/storage for a level).