class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        res = []
        q = s.split(' ')
        for i in q:
            if i.isdigit():
                if int(i) in res:
                    return False
                res.append(int(i))
        r = sorted(res)
        if r == res:
            return True
        else:
            return False
