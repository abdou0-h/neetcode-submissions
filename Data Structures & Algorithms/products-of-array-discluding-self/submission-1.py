class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def build_prefix_product(nums: list[int]) -> list[int]:
            prefix = [0] * len(nums)
            prefix[0] = 1

            for i in range(1, len(nums)):
                prefix[i] = prefix[i - 1] * nums[i - 1]

            return prefix

        def build_suffix_product(nums: list[int]) -> list[int]:
            suffix = [0] * len(nums)
            suffix[-1] = 1

            for i in range(len(nums) - 2, -1, -1):
                suffix[i] = suffix[i + 1] * nums[i + 1]

            return suffix

        prefix = build_prefix_product(nums)
        suffix = build_suffix_product(nums)
        res = []

        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[i])

        return res