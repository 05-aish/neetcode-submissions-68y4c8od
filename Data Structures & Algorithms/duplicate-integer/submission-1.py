class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        i = 0 
        j = 1
        n = len(nums) - 1
        for i in range(n):
            if(nums[i] == nums[j]):
                return True
            seen.append(nums[i])
            if nums[j] in seen:
                return True
            j = j + 1
        return False
        