# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        ans, temp = list(), list()
        count = 0
        while curr:
            temp.append(curr.val)
            count += 1
            if(count == k):
                ans.extend(temp[::-1])
                temp.clear()
                count = 0
            curr = curr.next

        ans.extend(temp)
        temp, i = head, 0
        while temp:
            temp.val = ans[i]
            temp = temp.next
            i += 1

        return head