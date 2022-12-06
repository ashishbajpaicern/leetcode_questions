# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        first = head
        second = head.next
        while first and second:
            if prev:
                prev.next = second
            else:
                head = second
            forward = second.next
            first.next = second.next
            second.next = first
            prev = first
            first = forward
            if not first:
                break
            second = first.next
        return head
