# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr, check = head, ""

        while curr:
            check += str(curr.val)
            curr = curr.next

        if(check == check[::-1]):
            return True
        return False