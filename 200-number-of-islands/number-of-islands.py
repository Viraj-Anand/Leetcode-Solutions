class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j,grid):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0':
                return
            
            grid[i][j]='0'
            bfs(i+1,j,grid)
            bfs(i,j+1,grid)
            bfs(i-1,j,grid)
            bfs(i,j-1,grid)

        m=len(grid)
        n=len(grid[0])
        count=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count+=1
    
                    bfs(i,j,grid)
        return count
          

        