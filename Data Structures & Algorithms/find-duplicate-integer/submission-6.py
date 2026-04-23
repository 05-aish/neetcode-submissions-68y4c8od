from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      n = len(nums)
      i = 0
      while(i < n):
        if nums[abs(nums[i]) - 1] < 0:
            return abs(nums[i])
        nums[abs(nums[i]) - 1] *= -1
        i += 1
         

# much optimised approach
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        raise ValueError("No duplicate value found")
    
        
# If the question asks for the duplicate number without modifying the array and requires indexing do let me know
    
            
