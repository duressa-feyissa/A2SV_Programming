class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        answer = []
        for key, value in nums1.items():
            if key in nums2:
                answer.extend([key]*min(value,nums2[key]))
        return answer
        