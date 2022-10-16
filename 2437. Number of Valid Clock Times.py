class Solution:
    def countTime(self, time: str) -> int:
        finaltime = ''
        res = 1
        if time[0] == '?' and time[1] == '?':
            res = res * 24
        if time[0] == '?' and time[1] < '4' and time[1] != '?':
            res = res * 3
        if time[0] == '?' and time[1] == '4' and time[1] != '?':
            res = res * 2
        if time[0] == '?' and time[1] > '4' and time[1] != '?':
            res = res * 2
        if time[1] == '?' and time[0] != '?':
            if time[0] == '0' or time[0] == '1':
                res = res * 10
            if time[0] == '2':
                res = res * 4

        if time[3] == '?' and time[4] == '?':
            res = res * 60
        if time[3] == '?' and time[4] != '?':
            res = res * 6
        if time[4] == '?' and time[3] != '?':
            res = res * 10

        return res
