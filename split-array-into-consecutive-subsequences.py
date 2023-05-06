class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        array = [(nums[0], 1)]
        N = len(nums)
        for i in range(1,N):
            if array[0][0] == nums[i]:
                heappush(array, (nums[i], 1))
            elif nums[i] - array[0][0] == 1:
                popped = heappop(array)
                updated = (nums[i], popped[1] + 1)
                heappush(array, updated)
            else:
                found = False
                while array and not found:
                    popped = heappop(array)
                    if nums[i] - popped[0] == 1:
                        heappush(array, (nums[i], popped[1] + 1))
                        found = True
                    elif popped[1] < 3:
                        return False
                if not found:
                    heappush(array, (nums[i], 1))
        for _, length in array:
            if length < 3:
                return False
        return True