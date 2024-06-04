
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        first_part = s[0:len(s) // 2]
        second_part = s[len(s) // 2:len(s)]



        if first_part == second_part:
            return True
        else:
            fp = ""
            sp = ""
            while len(first_part) < len(second_part):
                sp += second_part[0]
                second_part = second_part[1:]
            while not first_part == second_part:
                fp = first_part[-1] + fp
                first_part = first_part[:-1]

                sp += second_part[0]
                second_part = second_part[1:]

            if len(first_part) > 2 and first_part[0:len(fp + sp)] == fp + sp:
                return True
            elif first_part == fp + sp:
                return True
            else:
                return False
            