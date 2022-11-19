class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            if stack == []:
                stack.append(s[i])
            elif (ord(stack[-1]) == ord(s[i]) - 32) or (ord(stack[-1]) == ord(s[i]) + 32):
                stack = stack[:-1]
            else:
                stack.append(s[i])
        return ''.join(stack)
