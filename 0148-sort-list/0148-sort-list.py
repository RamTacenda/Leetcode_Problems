# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, ans, low, mid, high):
        temp = list()
        left, right = low, mid+1

        while(left <= mid and right <= high):
            if(ans[left] < ans[right]):
                temp.append(ans[left])
                left += 1
            else:
                temp.append(ans[right])
                right += 1

        while(left <= mid):
            temp.append(ans[left])
            left += 1
        while(right <= high):
            temp.append(ans[right])
            right += 1

        for i in range(0, len(temp)):
            ans[i + low] = temp[i]

    def mergesort(self, ans, low, high):
        if(low >= high):
            return
        mid = (low + high) // 2
        self.mergesort(ans, low, mid)
        self.mergesort(ans, mid+1, high)
        self.merge(ans, low, mid, high)
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans, curr, temp = list(), head, head
        while curr:
            ans.append(curr.val)
            curr = curr.next

        self.mergesort(ans, 0, len(ans)-1)

        idx = 0
        while temp:
            temp.val = ans[idx]
            temp = temp.next
            idx += 1

        return head