# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        length = overall = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        if length < k:
            return head

        overall = length - (length % k)

        curr, new_head = head, head
        prev = res = None
        count = k
        max_count = 0
        group_start = head
        prev_group_tail = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            count -= 1
            max_count += 1

            if count == 0:
                if res is None:
                    res = prev

                if prev_group_tail:
                    prev_group_tail.next = prev
                prev_group_tail = group_start
                group_start = tmp
                prev = None
                count = k

            if overall == max_count:
                break

        if prev_group_tail:
            prev_group_tail.next = curr

        return res


        