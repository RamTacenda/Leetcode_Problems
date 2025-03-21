class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Performing Topological sort to detect cycles using BFS
        adj = defaultdict(list)
        inComingEdges = [0]*(numCourses)
        toposort = []

        for after, before in prerequisites:
            adj[before].append(after)
            inComingEdges[after] += 1

        q = deque()
        for i in range(0, numCourses):
            if(inComingEdges[i] == 0):
                q.append(i)

        while q:
            node = q.popleft()
            toposort.append(node)
            for neighbour in adj[node]:
                inComingEdges[neighbour] -= 1
                if(inComingEdges[neighbour] == 0):
                    q.append(neighbour)

        return sum(inComingEdges) == 0