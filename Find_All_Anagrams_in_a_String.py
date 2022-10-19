class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pnum, snum = {}, {}
        for i in range(len(p)):
            pnum[p[i]] = 1 + pnum.get(p[i],0)
            snum[s[i]] = 1 + snum.get(s[i],0)
        if snum == pnum:
            res = [0]
        else:
            res = []
        l = 0
        for i in range(len(p),len(s)):
            snum[s[i]] = 1+snum.get(s[i],0)
            snum[s[l]] -= 1
            
            if snum[s[l]] == 0:
                snum.pop(s[l])
            l+=1
            if snum == pnum:
                res.append(l)
        return res
            
            
                
            
        
        
        
                
            
            
                
            
        
        
        
