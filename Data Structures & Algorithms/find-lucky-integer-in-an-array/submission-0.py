from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        max_lucky = -1
        
        for num, freq in counts.items():
            if num == freq:
                max_lucky = max(max_lucky, num)
                
        return max_lucky