class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        intersection = list((counter1 & counter2).elements())
        return intersection  