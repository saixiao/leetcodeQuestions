# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:   
        result = []
        temp = []
        bfs = [root, "#"]
        while len(bfs) > 1:
            node = bfs.pop(0)
            if node == None:
                continue
            if node == "#":
                result.append(temp)
                temp = []
                bfs.append("#")
                continue
            temp.append(node.val)
            bfs.append(node.left)
            bfs.append(node.right)
            
        return result[::-1]