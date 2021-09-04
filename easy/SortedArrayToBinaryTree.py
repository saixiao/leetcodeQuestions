# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        
        midPoint = len(nums) // 2
        root = TreeNode(nums[midPoint])
        
        # right
        self.createBinaryTree(root, nums[midPoint + 1:], True)
        # left
        self.createBinaryTree(root, nums[:midPoint], False)
        
        return root
    
    def createBinaryTree(self, root, nums, isRight):
        if root == None or len(nums) == 0:
            return
        
        midPoint = len(nums) // 2
        node = TreeNode(nums[midPoint])
        
        if isRight:
            root.right = node
        else:
            root.left = node
        
        # right
        self.createBinaryTree(node, nums[midPoint + 1:], True)
        # left
        self.createBinaryTree(node, nums[:midPoint], False)
        