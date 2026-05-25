class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        fresh=0
        moves = {(1,0), (-1,0), (0,1), (0,-1)}
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh +=1
        
        def isValid(r,c):
            if (r<0 or r>=ROWS or c<0 or c>=COLS or
                grid[r][c] == 0 or grid[r][c] == 2 or (r,c) in visited
            ):
                return False
            return True

        time = 0
        while fresh >0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                for move in moves:
                    newR = r + move[0]
                    newC = c + move[1]
                    if isValid(newR, newC):
                        q.append((newR, newC))
                        visited.add((newR, newC))
                        grid[newR][newC] = 2
                        fresh -= 1
            time += 1
        
        return time if fresh ==0 else -1


        