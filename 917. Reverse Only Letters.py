class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        l, r = 0, len(S)-1
        while l < r:
            if S[l].isalpha() and S[r].isalpha():
                S[l], S[r] = S[r], S[l]
                l += 1
                r -= 1
            else:
                if not S[l].isalpha():
                    l += 1
                if not S[r].isalpha():
                    r -= 1
        return ''.join(S)
