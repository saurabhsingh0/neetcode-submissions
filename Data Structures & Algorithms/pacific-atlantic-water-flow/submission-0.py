class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights), len(heights[0])
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def bfs(nodes):
            visited = set(nodes)
            queue = deque(nodes)
            while queue:
                r,c = queue.popleft()
                for dr, dc in moves:
                    nr,nc = r+dr, c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS \
                        and (nr, nc) not in visited \
                        and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited



        pacific_nodes = [(r,0) for r in range(ROWS)] + [(0,c) for c in range(COLS)]
        atlantic_nodes = [(r,COLS-1) for r in range(ROWS)] + [(ROWS-1,c) for c in range(COLS)]

        pacific = bfs(pacific_nodes)
        atlantic = bfs(atlantic_nodes)
        print(pacific)
        print(atlantic)
        return list(pacific & atlantic)

        