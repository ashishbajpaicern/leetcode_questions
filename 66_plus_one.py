class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            i = len(digits)-1
            while(digits[i] == 9 and i >= 0):
                digits[i] = 0
                i -= 1
            if(i >= 0):
                digits[i] += 1
            else:
                digits[0] = 1
                digits.append(0)

        else:
            digits[-1] = digits[-1] + 1
        return digits
