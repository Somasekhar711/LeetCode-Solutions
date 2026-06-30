from collections import defaultdict, deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n==1:
            return [0]
        graph=defaultdict(set)
        degree=[0]*n
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u]+=1
            degree[v]+=1
        q=deque()
        for i in range(n):
            if degree[i]==1:
                q.append(i)
        rem=n
        while rem>2:
            rem-=len(q)
            for i in range(len(q)):
                top=q.popleft()
                for nei in graph[top]:
                    degree[nei]-=1
                    graph[nei].remove(top)
                    if degree[nei]==1:
                        q.append(nei)

                graph[top].clear()
        return list(q)

# Approach: Use a topological sort-like approach to iteratively remove leaf nodes until 1 or 2 nodes remain, which are the roots of minimum height trees.
# Time Complexity: O(n) where n is the number of nodes, as each node and edge is processed once.
# Space Complexity: O(n) for the graph representation and degree array.