# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=[]
        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals=data.split(",")
        self.i=0
        def dfs():
            if vals[self.i]=="N":
                self.i+=1
                return None
            node=TreeNode(int(vals[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()

        

# Approach: Use preorder traversal with null markers to serialize the tree as a string, and rebuild the tree by reading tokens recursively during deserialization.
# Time Complexity: O(n) for both serialize and deserialize, where n is the number of nodes.
# Space Complexity: O(n) for the serialized token list and recursion stack in the worst case.

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))