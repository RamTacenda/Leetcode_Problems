# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_length(self, head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.get_length(head)
        curr = head

        if length == 1 and n == 1:
            return None

        if length == n:
            return head.next

        count = 0
        while curr:
            if(count == length-n-1):
                curr.next = curr.next.next
                break
            count += 1
            curr = curr.next

        return head