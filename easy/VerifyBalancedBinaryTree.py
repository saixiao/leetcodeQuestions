# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth, balanced = self.dfs(root)
        return balanced
        
        
    def dfs(self, root):
        if root == None:
            return 0, True
        
        rightDepth, br = self.dfs(root.right)
        leftDepth, bf = self.dfs(root.left)     
        rightDepth += 1
        leftDepth += 1
        
        balanced = br and bf and abs(rightDepth - leftDepth) <= 1

        return max(rightDepth, leftDepth), balanced