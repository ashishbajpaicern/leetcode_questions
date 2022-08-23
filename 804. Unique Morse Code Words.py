class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        coded = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",
                 ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-",
                 ".--", "-..-", "-.--", "--.."]
        res = set()
        for i in words:
            code = ''.join([coded[ord(j)-97] for j in i])
            res.add(code)
        return len(res)
