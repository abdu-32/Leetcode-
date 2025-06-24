class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = [str(i) for i in digits]
        a = str(int("".join(n)) + 1)
        ans = []
        for i in range(len(a)):
            ans.append(int(a[i]))
        return ans