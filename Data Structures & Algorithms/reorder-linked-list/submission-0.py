# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Count the length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Step 2: Split into two halves
        mid = (length + 1) // 2  # first half >= second half
        prev = None
        curr = head
        for _ in range(mid):
            prev = curr
            curr = curr.next
        prev.next = None  # terminate first half
        head2 = curr     # start of second half

        # Step 3: Reverse the second half
        prev = None
        curr = head2
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head2 = prev  # new head of reversed second half

        # Step 4: Merge the two halves
        first = head
        second = head2
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2