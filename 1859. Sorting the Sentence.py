class Solution:
    def sortSentence(self, s: str) -> str:
        l = []
        res = []
        r = ''
        a = s.split(" ")
        for i in a:
            l.append(i[-1])
        l.sort()
        for i in l:
            for j in a:
                if j[-1] == i:
                    res.append(j[:-1])
        return ' '.join(res)
