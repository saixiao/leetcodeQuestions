# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        level = 1
        
        bfsList = [root, "#"]
        
        while len(bfsList) > 1:
            node = bfsList.pop(0)
            
            if node == "#":
                level += 1
                bfsList.append("#")
                continue
            
            if node == None:
                continue
            
            if node.left == None and node.right == None:
                return level
            
            bfsList.append(node.left)
            bfsList.append(node.right)
            
        return level
        