from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Iterate through the array element by element
        for i in range(len(nums)):
            # Convert the number to a 0-based index by subtracting 1
            # We use abs() to get the original value even if it was negated
            index = abs(nums[i]) - 1
            
            # If the value at that index is already negative,
            # it means we have encountered this number before (it's the duplicate)
            if nums[index] < 0:
                return abs(nums[i])
            
            # Otherwise, mark the position as visited by flipping its sign to negative
            nums[index] *= -1
            
        # Return -1 if no duplicate is found (won't happen based on constraints)
        return -1