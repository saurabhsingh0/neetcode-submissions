class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        moves = {(1,0), (0,1), (-1,0), (0,-1)}
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        def isValidMove(r, c):
            if (r<0 or c<0 or r>=ROWS or c>=COLS 
                or (r,c) in visited or grid[r][c] == -1
            ):
                return False
            return True
        distance = 0
        while q:
            print(q)
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance
                for move in moves:
                    if isValidMove(r+move[0], c+move[1]):
                        q.append((r+move[0], c+move[1]))
                        visited.add((r+move[0], c+move[1]))

            distance += 1

        