# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.dfs(root, result, [], 0, targetSum)
        return result
        
        
    
    def dfs(self, root, result, path, currSum, target):
        if not root:
            return
        if not root.right and not root.left:
            path.append(root.val)
            if root.val + currSum == target:
                result.append(deepcopy(path))
            path.pop()
            return
        
        path.append(root.val)
        root.right and self.dfs(root.right, result, path, root.val + currSum, target)
        root.left and self.dfs(root.left, result, path, root.val + currSum, target)
        path.pop()
        