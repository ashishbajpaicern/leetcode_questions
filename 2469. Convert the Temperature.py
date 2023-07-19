class Solution:
    def convertTemperature(self, c: float) -> List[float]:
        k = c + 273.15
        f = c * 1.8 + 32.00
        return [k, f]
