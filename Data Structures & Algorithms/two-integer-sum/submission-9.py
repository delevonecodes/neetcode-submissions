class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i
        
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in mp and mp[compliment] != i:
                if i < mp[compliment]:
                    return [i, mp[compliment]]
                else:
                    return [mp[compliment], i]
