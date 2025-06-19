class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        s = set()
        for start , end in ranges:
            for i in range(start,end+1):
                s.add(i)

        for num in range(left,right+1):
            if num not in s:
                return False
            
        return True