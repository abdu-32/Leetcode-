class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for i in range(len(strs[0])):
            new_str=""
            for j in range(len(strs)):
                new_str += strs[j][i]

            if new_str != ''.join(sorted(new_str)):
                count+=1

        return count

            

        
