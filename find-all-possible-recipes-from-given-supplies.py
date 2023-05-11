class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        allRecipes = set(recipes)
        allSupplies = set(supplies)
        allIngredients = list(map(set,  ingredients))

        queue = deque([])
        N = len(recipes)
        required = defaultdict(int)
        answer = set()
        
        for i in range(N):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] not in allSupplies:
                    required[recipes[i]] += 1
        
        for i in range(N):
            if required[recipes[i]] == 0:
                queue.append(i)
                answer.add(i)

        while queue:
            popped = queue.popleft()
            for i in range(N):
                if recipes[popped] not in answer:
                    if recipes[popped] in allIngredients[i]:
                        required[recipes[i]] -= 1
                        if required[recipes[i]] == 0:
                            queue.append(i)
                            answer.add(i)
    
        return list(map(lambda x: recipes[x], answer))