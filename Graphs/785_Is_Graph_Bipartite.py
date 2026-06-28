from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        v=[0]*len(graph)
        q=deque()
        def bfs(i):
            if v[i]:
                return True
            v[i]=1
            q.append(i)
            while q:
                i=q.popleft()
                for nei in graph[i]:
                    if v[i]==v[nei]:
                        return False
                    elif not v[nei]:
                        v[nei]=-v[i]
                        q.append(nei)
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True


# Approach: Use BFS coloring to check graph bipartiteness by assigning opposite colors to neighbors.
# Time Complexity: O(V + E) where V is number of nodes and E is number of edges.
# Space Complexity: O(V) for the color array and BFS queue.
        