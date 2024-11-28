# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ls, curr = list(), head
        if head == None:
            return head
            
        while curr:
            ls.append(curr.val)
            curr = curr.next

        rotated, k = [0]*len(ls), (k % len(ls))
        for i in range(0, len(ls)):
            rotated[(i+k)%len(ls)] = ls[i]
        
        temp, idx = head, 0
        while temp:
            temp.val = rotated[idx]
            temp = temp.next
            idx += 1

        return head