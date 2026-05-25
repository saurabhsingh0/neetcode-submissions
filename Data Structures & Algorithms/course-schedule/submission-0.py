class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for u,v in prerequisites:
            adj[v].append(u)
            inDegree[u] += 1
        
        queue = deque()
        result = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        #queue = deque(i for i in range(numCourses) if inDegree[i] == 0)

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbour in adj[node]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return True if len(result) == numCourses else False

        