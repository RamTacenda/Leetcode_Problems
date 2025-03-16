# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append((root, 1))
        while q:
            root, depth = q.popleft()
            if not root.left and not root.right:
                return depth
            
            if root.left:
                q.append((root.left, depth+1))

            if root.right:
                q.append((root.right, depth+1))