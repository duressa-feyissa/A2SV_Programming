class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 1
        left =  0
        isSmall = 0
        for i in range(1, N):
            if nums[i] != nums[i - 1]:
                if nums[i] < nums[i - 1]:
                    isSmall = 1
                break
        count = 1
        while left < N:
            right = left + 1
            change = False
            if isSmall:
                while right < N and nums[right] < nums[right - 1]:
                    right += 1
                    change = True
                if change:
                    isSmall = isSmall ^ 1
                    count += 1
            else:
                while right < N and nums[right] > nums[right - 1]:
                    right += 1
                    change = True
                if change:
                    isSmall = isSmall ^ 1
                    count += 1
            if change:
                left = right - 1
            else:
                left += 1
        return count
            
            
            
            
        