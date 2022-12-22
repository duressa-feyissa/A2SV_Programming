class Solution:
    def freqAlphabets(self, s: str) -> str:
        new_dict = {}
        for i in range(97, 123):
            if i < 106:
                new_dict[str(i-96)] = chr(i)
            else:
                new_dict[str(i-96) + "#"] = chr(i)
        check = ["1", "2"]
        new = ""
        i = 0
        while i < len(s):
            if int(s[i]) > 2 and int(s[i]) < 10:
                new += new_dict[s[i]]
            elif s[i] in check:
                if i+2 < len(s):
                    if s[i + 2] == "#":
                        new += new_dict[s[i:i+3]]
                        i += 2
                    else:
                        new += new_dict[s[i]]
                if i == len(s) - 1 or i == len(s) - 2 :
                    if s[i] in check:
                        new += new_dict[s[i]]
            i+=1
        return new
                    
            
        