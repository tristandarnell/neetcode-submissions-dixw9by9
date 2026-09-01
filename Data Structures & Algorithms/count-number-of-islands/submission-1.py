class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate through rows, cols until hit a 1
        # create a helper method and run dfs 
        # that goes through up down left right dirs
        # iterate island count and set those u visited to 0
        # return # of islands
        
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    islands += 1
        return islands
