# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]

        mid = l + (r - l) // 2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)

        return self.mergeTwoList(left, right)
    def mergeTwoList(self , list1 , list2):
        dummy = curr = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next if list1.next else None
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next if list2.next else None
            curr = curr.next

        if list1:
            curr.next = list1

        elif list2:
            curr.next = list2
        return dummy.next


        