# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def post_order(self, node):
        elements = []
        if node.left:
            elements += self.post_order(node.left)
        if node.right:
            elements += self.post_order(node.right)
        elements.append(node.val)
        return elements
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.post_order(root)