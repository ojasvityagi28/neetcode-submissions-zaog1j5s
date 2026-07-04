# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedlist = []
            for i in range(0 ,len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedlist.append(self.mergeTwoList(l1 , l2))
            lists = mergedlist
        return lists[0]


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


        