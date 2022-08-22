# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            head = res = ListNode(min(list1.val, list2.val), None)
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                res.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                res.next = ListNode(list2.val, None)
                list2 = list2.next
            res = res.next
        if list1 != None:
            res.next = list1
        elif list2 != None:
            res.next = list2
        return (head.next)
