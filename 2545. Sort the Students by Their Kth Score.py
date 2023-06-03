class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        for i in range(len(score)):
            d[score[i][k]] = i
        l = list(d.keys())
        l.sort(reverse=True)
        sortD = {i: d[i] for i in l}
        res = []
        for i in sortD.keys():
            for j in range(len(score)):
                if score[j][k] == i:
                    res.append(score[j])
        return res
