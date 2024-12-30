class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t_mapping = {}
        t_to_s_mapping = {}

        for char_s, char_t in zip(s, t):
            if char_s not in s_to_t_mapping and char_t not in t_to_s_mapping:
                s_to_t_mapping[char_s] = char_t
                t_to_s_mapping[char_t] = char_s
            elif s_to_t_mapping.get(char_s) != char_t or t_to_s_mapping.get(char_t) != char_s:
                return False

        return True       