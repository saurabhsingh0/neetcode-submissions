import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * n
        adj = {i:[] for i in range(n)}
        for u, v, time in times:
            adj[u-1].append([v-1, time])
        dist[k-1] = 0
        min_heap = [(0,k-1)]
        while min_heap:
            time, u = heapq.heappop(min_heap)
            #print(time, u, dist)
            if time > dist[u]:
                continue
            for v, w in adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(min_heap, (dist[v], v))
        result = max(dist)
        return result if result != float('inf') else -1
        

        