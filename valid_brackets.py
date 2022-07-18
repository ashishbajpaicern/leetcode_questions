class Solution:
    def isValid(self, s: str) -> bool:

        from collections import deque

        l = deque()
        a = ["{", "[", "("]
        for i in range(len(s)):
            if s[i] in a:
                l.append(s[i])
            elif s[i] == ")":
                if not l or "(" not in l:
                    return False
                if l[-1] == "(":
                    l.pop()
            elif s[i] == "}":
                if not l or "{" not in l:
                    return False
                if l[-1] == "{":
                    l.pop()
            elif s[i] == "]":
                if not l or "[" not in l:
                    return False
                if l[-1] == "[":
                    l.pop()
        return not l
