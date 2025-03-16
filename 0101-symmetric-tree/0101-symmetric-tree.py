# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(leftsub, rightsub):
            if not leftsub and not rightsub:
                return True
            if not leftsub or not rightsub:
                return False
            return ((leftsub.val == rightsub.val) and 
                    check(leftsub.left, rightsub.right) and
                    check(leftsub.right, rightsub.left))
        return check(root.left, root.right)