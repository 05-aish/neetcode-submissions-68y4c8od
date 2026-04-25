class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        numsSet = set(nums)
        longest = 0
        for i in range(n):
            length = 0
            if (nums[i] - 1 not in numsSet):
                while nums[i] + length in nums:
                    length += 1
                longest = max(length, longest)
        return longest
                
            
