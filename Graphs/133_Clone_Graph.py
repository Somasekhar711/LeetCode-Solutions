# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        hashmap={}
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            copy=Node(node.val)
            hashmap[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)


# Approach: Use DFS + hashing to clone each node and its neighbors without revisiting copied nodes.
# Time Complexity: O(V + E) where V is number of nodes and E is number of edges in the graph.
# Space Complexity: O(V) for the recursion stack and hashmap of cloned nodes.
