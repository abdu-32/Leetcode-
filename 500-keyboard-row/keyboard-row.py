class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a="qwertyuiop"
        b="asdfghjkl"
        c="zxcvbnm"
        l=[]
        for i in words:
            cn1=0
            cn2=0
            cn3=0
            for char in i:
                if char.lower() in a:
                    cn1+=1
                if char.lower() in b:
                    cn2+=1
                if char.lower() in c:
                    cn3+=1
            if cn1==0 and cn2==0:
                l.append(i)
            if cn2==0 and cn3==0:
                l.append(i)
            if cn1==0 and cn3==0:
                l.append(i)
        return l