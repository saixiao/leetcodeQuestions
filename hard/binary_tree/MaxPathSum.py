# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')
        def dfs(root):
            if root == None:
                return float('-inf'), float('-inf')
            nonlocal max_path
            
            left_full_path, left_partial = dfs(root.left)
            right_full_path, right_partial = dfs(root.right)
            max_path = max(right_full_path, left_full_path, left_partial, right_partial, max_path)
            
            return left_partial + right_partial + root.val, max(left_partial + root.val, right_partial + root.val, root.val)
        
        a, b = dfs(root)
        return max(a, b, max_path)
        
        