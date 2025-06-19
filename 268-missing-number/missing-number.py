class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sets = set()
        lenght = len(nums)
        for i in range(lenght + 1):
            sets.add(i)
        diff = sets.difference(nums)
        for result in diff:
            return result
    

        