class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        end = ''
        start = ''
        extra = ''
        if ch not in word:
            return word
        for i in range(len(word)):
            if word[i] == ch:
                end = word[i:]
                break
            else:
                start = start + word[i]
        extra = start[::-1]
        return (ch + extra + end[1:])
