class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = self.compare(nums, 0, len(nums)-1, True)
        if score[0] >= score[1]:
            return True
        return False
    def compare(self, nums, left, right, turn):
        if left == right:
            if turn:
                return [nums[left], 0]
            else:
                return [0, nums[left]]
        
        if turn:
            resultRight = self.compare(nums, left, right - 1, not turn)
            resultRight[0] += nums[right]
            resultLeft = self.compare(nums, left + 1, right, not turn)
            resultLeft[0] += nums[left]
            if resultRight[0] >= resultLeft[0]:
                return resultRight
            return resultLeft
        else:
            resultRight = self.compare(nums, left, right - 1, not turn)
            resultRight[1] += nums[right]
            resultLeft = self.compare(nums, left + 1, right, not turn)
            resultLeft[1] += nums[left]
            if resultRight[1] >= resultLeft[1]:
                return resultRight
            return resultLeft