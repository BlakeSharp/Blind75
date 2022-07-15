# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        result= ListNode()
        test = result

        while(list1 and list2):
            if(list2.val<=list1.val):
                test.next = list2
                list2 = list2.next
            else:
                test.next = list1
                list1 = list1.next
            test = test.next

        if(list1):
            test.next = list1
        else:
            test.next = list2

        return result.next
