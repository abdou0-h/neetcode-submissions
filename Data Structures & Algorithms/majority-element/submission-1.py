from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        majority_count = len(nums) // 2
        
        for num, count in counts.items():
            if count > majority_count:
                return num