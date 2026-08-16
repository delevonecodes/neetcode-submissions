import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return []
        n = len(nums)
        prefix = [0 for i in range(n)]
        suffix = [0 for i in range(n)]

        for i in range(n):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = math.prod(nums[:i])
        
        for i in range(n):
            if i == n:
                suffix[i] = 1
            else:
                suffix[i] = math.prod(nums[i+1:])

        return [p * s for p, s in zip(prefix, suffix)]
        
    
