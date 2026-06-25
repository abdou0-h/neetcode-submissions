class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        counts = Counter(nums)
        majority_count = len(nums) // 3
        
        for num, count in counts.items():
            if count > majority_count:
                res.append(num)
        
        return res