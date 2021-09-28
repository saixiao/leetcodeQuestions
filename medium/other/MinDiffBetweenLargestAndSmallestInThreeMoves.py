class Solution:
    def minDifference(self, nums: List[int], int: k) -> int:
        nums.sort()
        return min((b - a for a,b in zip(nums[:k], nums[-k:])))