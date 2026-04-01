# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        prev = None
        curr = head
        for  i in range(length):
            if i==(length//2):
                end_1stlist = curr
            if i >= (length//2 + 1):
                tmp = curr.next 
                curr.next = prev
                prev = curr
                curr = tmp
            else:
                curr = curr.next
        head2 = prev #because will curr be None
        end_1stlist.next = None
        while head2:
            tmp1 = head.next
            tmp2 = head2.next
            head.next = head2
            head2.next = tmp1
            head = tmp1
            head2 = tmp2
    



        