# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check = []
        if head is None:
            return None
        while(head != None):

            check.append(head.val)
            head = head.next
        return check == check[::-1]
