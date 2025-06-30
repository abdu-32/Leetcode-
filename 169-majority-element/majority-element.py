class Solution:
    def majorityElement(self, nums):
        counts = {}
        majority_count = len(nums) // 2

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

            if counts[num] > majority_count:
                return num
