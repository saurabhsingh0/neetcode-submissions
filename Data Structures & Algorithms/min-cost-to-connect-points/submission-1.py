class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range (N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visited= set()
        min_heap = [[0,0]]
        while len(visited) < N:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for nei_cost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(min_heap, [nei_cost, nei])
        
        return res