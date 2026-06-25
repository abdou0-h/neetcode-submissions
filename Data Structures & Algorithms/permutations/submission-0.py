from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # 1. Sort the array so that identical numbers are next to each other
        # This is essential to easily detect and skip duplicates
        nums.sort()
        
        # 2. Track which elements (cards) are currently placed inside our boxes
        # False means the card is still in our hand, True means it's in a box
        used = [False] * len(nums)
        
        def play(path):
            # Base Case: If the current box sequence (path) is full
            # we found a valid permutation, so we save a copy of it
            if len(path) == len(nums):
                res.append(path.copy())
                return # Go back (Backtrack) to explore other choices
            
            # Try placing every available card into the current box
            for i in range(len(nums)):
                
                # Check 1: If this specific card is already used in a box, skip it
                if used[i]:
                    continue
                
                # ---- Forward Move (Make Choice) ----
                used[i] = True         # Mark the card as used
                path.append(nums[i])   # Put the card into the current box
                
                # Move to the next box (Go deeper into the decision tree)
                play(path)
                
                # ---- Backward Move (Backtrack / Undo Choice) ----
                path.pop()             # Take the card out of the box
                used[i] = False        # Return the card back to our hand
                
        # Start the game with an empty box sequence
        play([])
        
        return res