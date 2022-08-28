class Solution:
    def capitalizeTitle(self, title: str) -> str:
        temp = title.split()
        res = []
        for i in temp:
            if len(i) < 3:
                res.append(i.lower())
            else:
                res.append(i.capitalize())
        return " ".join(res)
