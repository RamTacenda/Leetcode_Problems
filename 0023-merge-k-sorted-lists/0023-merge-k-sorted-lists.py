# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heaps = []
        for i, node in enumerate(lists):
            if node:
                heaps.append((node.val, i, node))

        heapq.heapify(heaps)
        
        dummy = ListNode()
        curr = dummy

        while heaps:
            val, idx, node = heapq.heappop(heaps)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heaps, (node.val, idx, node))
        
        return dummy.next