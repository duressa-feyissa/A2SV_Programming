class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        dictionary = {}
        for domain in cpdomains:
            value = domain.split()
            times = int(value[0])
            subdomains = value[1].split(".")
            if len(subdomains) == 3:
                key1 = subdomains[0] + "." + subdomains[1] + "." + subdomains[2]
                key2 = subdomains[1] + "." + subdomains[2]
                key3 = subdomains[2]
                keys = [key1, key2, key3]
                
                for key in keys:
                    if key in dictionary:
                        dictionary[key] += times
                    else:
                        dictionary[key] = times
            
            elif len(subdomains) == 2:
                key1 = subdomains[0] + "." + subdomains[1]
                key2 = subdomains[1]
                keys = [key1, key2]
                
                for key in keys:
                    if key in dictionary:
                        dictionary[key] += times
                    else:
                        dictionary[key] = times
            
        answer = []
        for key, value in dictionary.items():
            answer.append(str(value) + " " + key)
            
        return answer
            
            
            
                