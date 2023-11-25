class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        while list1 or list2:
            x = list1.val if list1 else float('inf')
            y = list2.val if list2 else float('inf')

            if x < y:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        return dummy.next