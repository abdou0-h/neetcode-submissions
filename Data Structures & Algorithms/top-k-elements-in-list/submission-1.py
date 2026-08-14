class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        result = sorted(hash_map.items(), key = lambda x: x[1], reverse = True)
        i = 0
        res = []
        while k > 0:
            
            res.append(result[i][0])
            i += 1
            k -= 1
        
        return res
