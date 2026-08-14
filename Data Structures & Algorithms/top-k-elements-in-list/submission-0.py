class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {key: 0 for key in nums}

        for key in nums:
            hash_map[key] += 1
        
        result = sorted(hash_map.items(), key = lambda x: x[1], reverse = True)
        i = 0
        res = []
        while k > 0:
            
            res.append(result[i][0])
            i += 1
            k -= 1
        
        return res


