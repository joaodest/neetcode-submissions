# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    CURR_LEN = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lfind = self.maxDepth(root.left)
        rfind = self.maxDepth(root.right)
        return 1 + max(lfind, rfind)