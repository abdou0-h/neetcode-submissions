class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        counts = Counter(nums)

        for i, element in counts.items():


            if element >= 2:
                return True
        
        return False