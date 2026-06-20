# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        paths = []

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            if not node.left and not node.right:
                paths.append(path)
                return

            path += "->"

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return paths

# Approach: DFS with Path Accumulation (Backtracking)
# Time Complexity: O(n * h) - Visit n nodes, string concatenation takes O(h) per node
# Space Complexity: O(h) - Call stack depth, h = tree height