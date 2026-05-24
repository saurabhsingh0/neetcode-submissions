class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] ==1:
                    newArea = self.areaOfIsland(grid, r,c, visited)
                    print(newArea)
                    maxArea = max(maxArea, newArea)
        
        return maxArea

    def areaOfIsland(self, grid:List[List[int]], i, j, visited):
        print(i,j)
        visited.add((i,j))
        moves = {(1,0), (0,1), (-1,0), (0,-1)}
        area = 1
        def isValidMove(grid, i, j, visited):
            rows,cols = len(grid), len(grid[0])
            if i<0 or j<0 or i>=rows or j>=cols or (i,j) in visited or grid[i][j] == 0:
                return False
            return True
        for move in moves:
            ni = i + move[0]
            nj = j + move[1]
            if isValidMove(grid, ni, nj, visited):
                area = area + self.areaOfIsland(grid, ni, nj, visited)
        
        return area
        