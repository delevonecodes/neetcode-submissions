class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 3:
            return [0,1]

        hmap = {}
        for i, num in enumerate(nums):
            hmap[num] = i
        for i in range(len(nums)):
            num = nums[i]
            c2 = target - num
            if c2 in hmap and hmap[c2] != i:
                return [i, hmap[c2]]