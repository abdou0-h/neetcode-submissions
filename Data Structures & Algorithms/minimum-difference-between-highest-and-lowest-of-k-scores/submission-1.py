class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:

        if k == 1:
            return 0
        
        nums.sort()
        min_diff = float('inf')
        
        for i in range(k - 1, len(nums)):
            current_diff = nums[i] - nums[i - k + 1]
            min_diff = min(min_diff, current_diff)
            
        return min_diff