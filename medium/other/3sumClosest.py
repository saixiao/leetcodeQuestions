class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                
                if abs(target - result) > abs(target - s):
                    result = s
                
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
        
        return result