class Solution(object):
    def findCircleNum(self, isConnected):
        parent=[0]*len(isConnected)
        for i in range(len(parent)):
            parent[i]=i
        provinces=len(parent)
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def unionFind(x,y,provinces):
            parent_x=find(x)
            parent_y=find(y)
            if parent_x!=parent_y:
                parent[parent_x]=parent[parent_y]
                provinces-=1
            return provinces
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1:
                    provinces=unionFind(i,j,provinces)
        return provinces


# Approach: Use union-find to merge connected cities and count connected components as provinces.
# Time Complexity: O(n^2 * α(n^2)) where n is number of cities and α is inverse Ackermann.
# Space Complexity: O(n^2) for the parent array and recursion in find path compression.
