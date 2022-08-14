class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()

        if s == "":
            return 0

        pos_limit = 2147483647
        neg_limit = -2147483648

        neg = False
        if s[0] == '-':
            neg = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        else:
            pass

        result = 0
        for value in s:
            if not value.isdigit():
                break

            result = (result * 10) + int(value)

        if neg:
            if (-1*result) < neg_limit:
                return neg_limit

            return -1 * result
        else:
            if result > pos_limit:
                return pos_limit

            return result
