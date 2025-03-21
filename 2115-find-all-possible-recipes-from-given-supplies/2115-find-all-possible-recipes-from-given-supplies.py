class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        inDegree = {recipe: 0 for recipe in recipes}

        # Building graph and calculating indegrees
        for i in range(0, len(recipes)):
            for ingred in ingredients[i]:
                adj[ingred].append(recipes[i])
            inDegree[recipes[i]] = len(ingredients[i])

        # Initilizing the queue
        res = []
        q = deque(supplies)

        # BFS to find all possible recipe
        while q:
            node = q.popleft()
            for recipe in adj[node]:
                inDegree[recipe] -= 1
                if(inDegree[recipe] == 0):
                    res.append(recipe)
                    q.append(recipe)
        return res