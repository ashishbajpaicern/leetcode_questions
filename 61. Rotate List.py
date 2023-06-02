class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        # Calculate the length of the linked list
        length = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            length += 1

        # Adjust the value of k to be within the range of the list length
        k = k % length

        # No rotation needed
        if k == 0:
            return head

        # Find the new head and tail nodes after rotation
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # Make the new tail node point to None
        new_tail.next = None

        # Attach the old tail node to the original head to form a cycle
        tail.next = head

        return new_head
