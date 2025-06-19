class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        se = set()
        for start , end in ranges:
            for i in range(start,end+1):
                se.add(i)

        for num in range(left,right+1):
            if num not in se:
                return False
            
        return True