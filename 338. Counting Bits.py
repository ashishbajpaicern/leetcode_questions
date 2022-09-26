class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        res = []
        sum = 0
        for i in range(n+1):
            a = format(i, "b")
            l.append(a)
        for z in range(len(l)):
            sum = 0
            i = int(l[z])
            while i > 0:
                temp = i % 10
                sum = sum + temp
                i = i // 10
            res.append(sum)
        return (res)
