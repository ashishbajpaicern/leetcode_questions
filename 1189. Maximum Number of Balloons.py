class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'b': 0,
             'a': 0,
             'l': 0,
             'o': 0,
             'n': 0}
        for i in text:
            if i in d:
                d[i] += 1
        count = 0
        while True:
            if d['b'] > 0:
                d['b'] -= 1
            else:
                break
            if d['a'] > 0:
                d['a'] -= 1
            else:
                break
            if d['l'] > 1:
                d['l'] -= 2
            else:
                break
            if d['o'] > 1:
                d['o'] -= 2
            else:
                break
            if d['n'] > 0:
                d['n'] -= 1
            else:
                break
            count += 1
        return count
