class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans = []

        for i in range(len(s)):
            if s[i] in ans:
                continue

            while ans and s[i] < ans[-1] and ans[-1] in s[i+1:]:
                ans.pop()

            ans.append(s[i])

        return "".join(ans)
