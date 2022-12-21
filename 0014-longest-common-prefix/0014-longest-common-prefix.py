class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """    
        if len(strs) == 1:
            return strs[0]
        
        num = float('inf')
        for i in strs:
            num = min(num, len(i))
                
        i = 0
        prefix = ""
        while i < num:
            j = 0
            if i < len(strs[0]):
                flag = strs[0][i]
            else:
                return prefix
            while j < len(strs):
                if i >= len(strs[j]):
                    return prefix
                if flag != strs[j][i]:
                    return prefix
                j+=1
            i+=1
            prefix += flag
        return prefix
            
        