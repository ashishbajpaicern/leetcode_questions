class Solution:
    def maximum69Number(self, num: int) -> int:
        l = str(num)
        l = list(l)
        for i in range(len(l)):
            if l[i] == '6':
                l[i] = '9'
                break
        z = ''.join(l)
        return int(z)
