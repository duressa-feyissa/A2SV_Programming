class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        content = {}
        
        for path in paths:
            path = path.split()
            
            for idx, item in enumerate(path):
                if idx == 0:
                    continue
                index = item.index("(")
                key = item[index+1:-1]
                if key in content:
                    content[key].append(path[0] + "/" + path[idx][:index])
                else:
                    content[key] = []
                    content[key].append(path[0] + "/" + path[idx][:index])
        
        answer = []
        for value in content.values():
            if len(value) > 1:
                answer.append(value)
        return answer
        