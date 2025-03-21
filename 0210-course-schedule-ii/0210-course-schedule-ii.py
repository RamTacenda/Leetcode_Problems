class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(0, numCourses)]
        inDegree = [0]*numCourses
        for after, before in prerequisites:
            inDegree[after] += 1
            adj[before].append(after)

        print(adj)
        
        order = []
        q = deque()
        for i in range(0, numCourses):
            if(inDegree[i] == 0):
                q.append(i)
        print(q)

        while q:
            node = q.popleft()
            order.append(node)
            for neighbour in adj[node]:
                inDegree[neighbour] -= 1
                if(inDegree[neighbour] == 0):
                    q.append(neighbour)

        return order if(sum(inDegree) == 0) else [] 