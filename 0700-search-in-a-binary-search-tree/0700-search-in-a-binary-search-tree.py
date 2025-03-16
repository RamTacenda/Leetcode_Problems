# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def check(root, val):
            if val == root.val:
                return root
            elif val < root.val:
                if root.left:
                    return check(root.left, val)
            elif val > root.val:
                if root.right:
                    return check(root.right, val)
        
        return check(root, val)