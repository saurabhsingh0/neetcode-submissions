class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for u,v in prerequisites:
            inDegree[u] += 1
            adj[v].append(u)
        
        queue = deque(i for i in range(len(inDegree)) if inDegree[i] == 0)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbour in adj[node]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return result if len(result) == numCourses else []