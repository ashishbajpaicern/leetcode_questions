# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        s = 0  # Initialize a variable to store the sum
        tmp = head  # Store the original head
        prev = None  # Initialize a variable to keep track of the previous zero node
        merged_head = None  # Initialize a variable to store the head of the merged list

        while head is not None:
            if head.val == 0:
                if s != 0:
                    zero_node = ListNode(s)  # Create a new node with the sum
                    if merged_head is None:
                        merged_head = zero_node
                        prev = zero_node
                    else:
                        prev.next = zero_node
                        prev = zero_node
                s = 0  # Reset the sum
            else:
                s += head.val  # Add the value to the sum

            head = head.next  # Move to the next node

        return merged_head
