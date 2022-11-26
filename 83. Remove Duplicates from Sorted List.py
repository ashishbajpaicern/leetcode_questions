# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        prev = head
        if head == None:
            return None
        while head.next != None:
            head = head.next
            if head.val == prev.val:
                prev.next = head.next
            else:
                prev = head
        return res
