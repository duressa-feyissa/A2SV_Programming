class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hash_map = {}
        stack = []
        n = len(nums2)
        for index in range(n - 1, -1, -1):
            while stack and stack[-1] < nums2[index]:
                stack.pop()
            if not stack:
                hash_map[nums2[index]] = -1
            else:
                hash_map[nums2[index]] = stack[-1]
            stack.append(nums2[index])
        
        answer = []
        for num in nums1:
            answer.append(hash_map[num])
        
        return answer
            
                
        
        