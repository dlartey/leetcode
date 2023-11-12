# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        ans = ListNode(-1)
        dummy = ans

        while l1 or l2 or rem:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = (val1 + val2 + rem)

            if (total > 9):
                total = total % 10
                rem = 1
            else:
                rem = 0

            ans.next = ListNode(total)
            ans = ans.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        
        return dummy.next



        