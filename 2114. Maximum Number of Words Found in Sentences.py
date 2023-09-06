class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0
        for i in sentences:
            l = i.count(" ")
            if m < l:
                m = l
        return m + 1
