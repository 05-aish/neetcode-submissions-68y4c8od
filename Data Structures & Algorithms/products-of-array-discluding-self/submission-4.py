class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = [1]
        suffix = [1] * len(nums)

        productPrefix = 1
        for i in range(1, len(nums)):
            productPrefix *= nums[i - 1]
            prefix.append(productPrefix)

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(len(prefix)):
            res[i] = prefix[i] * suffix[i]

        return res


            
