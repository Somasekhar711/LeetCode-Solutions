class Solution(object):
    def numIslands(self, grid):
        row=len(grid)
        col=len(grid[0])
        visit=set()
        parent=[0]*(row*col)
        for i in range(row*col):
            parent[i]=i
        islands=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1":
                    islands+=1
        def find(idx):
            if parent[idx]!=idx:
                parent[idx]=find(parent[idx])
            return parent[idx]
        def union(i,j,islands):
            parent_i=find(i)
            parent_j=find(j)
            if parent_i!=parent_j:
                parent[parent_i]=parent[parent_j]
                islands-=1
            return islands
            
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1":
                    cur_idx=r*col+c

                    for nr,nc in [(r+1,c),(r,c+1)]:
                        if nr<row and nc < col and grid[nr][nc]=="1":
                            neighbour_idx=nr*col+nc
                            islands=union(cur_idx,neighbour_idx,islands)
        return islands


# Approach: Use union-find to merge adjacent land cells and count connected island components.
# Time Complexity: O(m * n * α(m * n)) where α is the inverse Ackermann function.
# Space Complexity: O(m * n) for the parent array.
        