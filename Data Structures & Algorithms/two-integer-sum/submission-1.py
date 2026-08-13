class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {key: index for index, key in enumerate(nums)}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hash_map and i != hash_map[diff]:
                res = [i, hash_map[diff]]
                res.sort()
                return res
