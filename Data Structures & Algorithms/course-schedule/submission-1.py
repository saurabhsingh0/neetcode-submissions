class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        
        UNVISITED, VISITING, VISITED = 0, 1, 2
        #mark everynode as unvisited
        state = [UNVISITED] * numCourses
        stack = []
        hasCycle = [False]

        def dfs(node):
            if hasCycle[0]:
                return
            state[node] = VISITING
            for neighbour in adj[node]:
                if state[neighbour] == VISITING:
                    hasCycle[0] = True
                    return
                if state[neighbour] == UNVISITED:
                    dfs(neighbour)
            state[node] = VISITED
            stack.append(node)


        for i in range(numCourses):
            if state[i] == UNVISITED:
                dfs(i)
        
        return False if hasCycle[0] else True

        