class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if start.replace('X', '') != result.replace('X', ''):
            return False

        pos_start_LR = [(char, idx) for idx, char in enumerate(start) if char in "LR"]
        pos_result_LR = [(char, idx) for idx, char in enumerate(result) if char in "LR"]

        for (char_s, idx_s), (char_r, idx_r) in zip(pos_start_LR, pos_result_LR):
            if char_s != char_r:
                return False
            if char_s == 'L' and idx_s < idx_r:
                return False
            if char_s == 'R' and idx_s > idx_r:
                return False

        return True
