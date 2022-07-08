class Solution:
    def isPalindrome(self, x: int) -> bool:
        start = x
        end = 0
        while(x > 0):
            Reminder = x % 10
            end = (end * 10) + Reminder
            x = x // 10
        if start == end:
            return True
        else:
            return False
