class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = list(s)
        tt = list(t)
        st.sort()
        tt.sort()
        if st == tt:
            return True
        else:
            return False
