class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        closest = float("inf")
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if closest == 0:
                return sum(result)

            res, c = self.twoSum(closest, target - nums[i], i, nums, nums[i])

            if c < closest:
                result = res
                closest = c
        
        return sum(result)
    
    def twoSum(self, closest, target, i, nums, current_number):
        lptr = 0
        rptr = len(nums) - 1
        result = []
        
        while lptr < rptr:
            if lptr == i:
                lptr += 1
                continue
            elif rptr == i:
                rptr -= 1
                continue
            
            curr_sum = nums[lptr] + nums[rptr]
            
            if abs(target - curr_sum) == 0:
                return [current_number, nums[lptr], nums[rptr]], 0

            if abs(target - curr_sum) < closest:
                closest = abs(target - curr_sum)
                result = [current_number, nums[lptr], nums[rptr]]
            
            if target - curr_sum > 0:
                lptr += 1
            elif target - curr_sum < 0:
                rptr -= 1
                
        return result, closest
                