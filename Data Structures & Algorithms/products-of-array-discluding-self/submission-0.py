import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return []
        hmap = {}
        for i in range(len(nums)):
            hmap[i] = [num for y, num in enumerate(nums) if y != i]
        output = []     
        for l in hmap.values():
            output.append(math.prod(l))
        return output

