class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even = 0
        for left in nums:
            if left % 2 == 0:
                even+=left

        answer = []
        for query in queries:
            if query[0] % 2 == 0:
                if nums[query[1]] % 2 == 0:
                    even += query[0]
                    answer.append(even)
                else:
                    answer.append(even)
            else:
                if nums[query[1]] % 2 == 0:
                    even -= nums[query[1]]
                    answer.append(even)
                else:
                    even += query[0] + nums[query[1]]
                    answer.append(even)
            nums[query[1]] += query[0]
        return answer
                    
                    
        