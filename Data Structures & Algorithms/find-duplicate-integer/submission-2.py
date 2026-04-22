class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      n = len(nums)
      i = 0
      s = set()
      while(i < n):
        
        s.add(nums[i])
        i += 1
        if nums[i] in s:
            return nums[i]
        
    
            
