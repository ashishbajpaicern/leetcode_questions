class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if curr == "(":
                    if char != ")":
                        return False
                if curr == "{":
                    if char != "}":
                        return False
                if curr == "[":
                    if char != "]":
                        return False

        if stack:
            return False
        return True
