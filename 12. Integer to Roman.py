class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        while num > 0:
            if num - 1000 >= 0:
                num = num - 1000
                res = res + 'M'
                continue
            if num - 900 >= 0:
                num = num - 900
                res = res + 'CM'
                continue
            if num - 500 >= 0:
                num = num - 500
                res = res + 'D'
                continue
            if num - 400 >= 0:
                num = num - 400
                res = res + 'CD'
                continue
            if num - 100 >= 0:
                num = num - 100
                res = res + 'C'
                continue
            if num - 90 >= 0:
                num = num - 90
                res = res + 'XC'
                continue
            if num - 50 >= 0:
                num = num - 50
                res = res + 'L'
                continue
            if num - 40 >= 0:
                num = num - 40
                res = res + 'XL'
                continue
            if num - 10 >= 0:
                num = num - 10
                res = res + 'X'
                continue
            if num - 9 >= 0:
                num = num - 9
                res = res + 'IX'
                continue
            if num - 5 >= 0:
                num = num - 5
                res = res + 'V'
                continue
            if num - 4 >= 0:
                num = num - 4
                res = res + 'IV'
                continue
            if num - 1 >= 0:
                num = num - 1
                res = res + 'I'
                continue
        return res
