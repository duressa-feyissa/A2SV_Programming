class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        check = {"*": 0, "/*": 0, "//":0} 
        
        answer = []
        string = ""
        
        for index, item in enumerate(source):
            left = 0
            while left < len(item):
                
                if item[left] == "/":
                    if left + 1 < len(item) and item[left + 1] == "/":
                        if check["/*"] == 0:
                            if len(string):
                                answer.append(string)
                            string=""
                            check["//"] = 1
                            check["*"] = 0
                            break
                    if  left + 1 < len(item) and item[left + 1] == "*":
                        check["/*"] = 1    

                if check["/*"] == 0:
                    string += item[left]
                
                if item[left] == "*" and check["/*"] == 1:
                    check["*"] += 1
                    if check["*"] > 1:
                        if left + 1 < len(item) and item[left + 1] == "/" and check["/*"]:
                            check["/*"] = 0
                            check["*"] = 0
                            left+=1
                left+=1
            if check["//"] == 1:
                check["//"] = 0
                continue
            if check["/*"] == 0 and len(string) != 0:
                answer.append(string)
                string=""
        return answer