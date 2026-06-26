from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph=[[] for _ in range(numCourses)]
        order=[]
        inDegree=[0]*numCourses
        for course,prereq in prerequisites:
            graph[prereq].append(course)
            inDegree[course]+=1
        q=deque()
        for i,degree in enumerate(inDegree):
            if degree==0:
                q.append(i)
        while q:
            top=q.popleft()
            order.append(top)
            for course in graph[top]:
                inDegree[course]-=1
                if inDegree[course]==0:
                    q.append(course)
        if len(order)!=numCourses:
            return []
        return order
# Approach: Use Kahn's algorithm for topological sort / BFS on indegree-zero nodes to find a valid course order.
# Time Complexity: O(V + E) where V is numCourses and E is prerequisites length
# Space Complexity: O(V + E) for the graph and indegree structures.