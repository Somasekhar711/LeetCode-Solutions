from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, preq in prerequisites:
            graph[preq].append(course)
            indegree[course] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0

        while q:
            node = q.popleft()
            count += 1

            for i in graph[node]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    q.append(i)

        return count == numCourses


# Approach: Use Kahn's algorithm for topological sort / BFS on indegree-zero nodes to detect cycles.
# Time Complexity: O(V + E) where V is numCourses and E is prerequisites length.
# Space Complexity: O(V + E) for the graph and indegree structures.