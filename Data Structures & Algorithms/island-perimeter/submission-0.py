class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        moves = {(-1,0), (1,0), (0,1), (0,-1)}
        visited = set()
                
        def dfs(i, j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]==0:
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            perimeter = 0
            for move in moves:
                perimeter += dfs(i+move[0], j+move[1])
            return perimeter 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r,c)

        return 0   
        