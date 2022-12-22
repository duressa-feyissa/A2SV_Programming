class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        new_dict1 = {}
        for i in s:
            if i in new_dict1:
                new_dict1[i]+=1
            else:
                new_dict1[i]=1
        new_dict2 = {}
        for i in t:
            if i in new_dict2:
                new_dict2[i]+=1
            else:
                new_dict2[i]=1
        for k in new_dict1.keys():
            new_dict2[k] = new_dict2[k] - new_dict1[k]
        for k in new_dict2.keys():
            if new_dict2[k] > 0:
                return k

        