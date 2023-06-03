class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        s.append(chars[0])
        count = 0
        check = []
        for i in range(len(chars)):
            if s[-1] == chars[i]:
                count += 1
            else:
                if count > 1:
                    if count < 10:
                        s.append(str(count))
                    else:
                        while count > 0:
                            tmp = count % 10
                            count = count // 10
                            check.append(str(tmp))
                        s.extend(check[::-1])
                        check = []
                s.append(chars[i])
                count = 1
        if count > 1:
            if count < 10:
                s.append(str(count))
            else:
                while count > 0:
                    tmp = count % 10
                    count = count // 10
                    check.append(str(tmp))
                s.extend(check[::-1])
                check = []

        for i in range(len(s)):
            chars[i] = s[i]
        l = len(chars)
        while l > len(s):
            chars.pop(-1)
            l -= 1
        return len(s)
