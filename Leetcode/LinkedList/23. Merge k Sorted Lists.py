# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        # IDEA: Use a PQ to store at most length items, in a pair of (value,listNo)
        # we pop the min. Then if listNo is not None, we append the next to the PQ
        # Continue this until PQ is empty, appending the smallest to the new list
        # then we return the new list

        heap = []

        for x in range(len(lists)):
            if lists[x]:
                heapq.heappush(heap,(lists[x].val,x))
                lists[x] = lists[x].next

        ans = ListNode(-1)
        dummy = ans

        while heap:
            value,index = heapq.heappop(heap)
            # (val, listNo)
            # if there's still values, then add the next to the heap
            if (lists[index]):
                heapq.heappush(heap,(lists[index].val,index))
                lists[index] = lists[index].next

            ans.next = ListNode(value)
            ans = ans.next

        return dummy.next
        