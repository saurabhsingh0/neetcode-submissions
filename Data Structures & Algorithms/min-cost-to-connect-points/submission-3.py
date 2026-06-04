class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        parent = list(range(N))
        rank = [0] * N
        edges = []

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y) -> bool:
            px, py = find(x), find(y)
            if  px == py:
                return False
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
            return True

        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append([dist, i, j])
        
        edges.sort()
        minCost = 0

        for dist, u, v in edges:
            if union(u, v):
                minCost += dist
        
        return minCost


        