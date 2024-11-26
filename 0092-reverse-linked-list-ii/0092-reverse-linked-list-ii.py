# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr, count = head, 1
        temp, elements = head, []
        while curr:
            if(count >= left and count <= right):
                elements.append(curr.val)
            count += 1
            curr = curr.next

        count = 1
        while temp:
            if(count >= left and count <= right):
                temp.val = elements.pop()
            count += 1
            temp = temp.next

        return head