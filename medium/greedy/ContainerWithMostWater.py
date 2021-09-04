class Solution:
    def maxArea(self, height: List[int]) -> int:
        rightPtr, leftPtr, maxWater = len(height) - 1, 0, 0
        
        while leftPtr != rightPtr:
            lh, rh, width = height[leftPtr], height[rightPtr], rightPtr - leftPtr
            maxWater = max(maxWater, min(lh, rh) * width)
            
            if lh > rh:
                rightPtr -= 1
            else:
                leftPtr += 1
        
        return maxWater
