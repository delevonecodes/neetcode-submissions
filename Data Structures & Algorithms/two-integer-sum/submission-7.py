class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        mp = {}
        for i, num in enumerate(nums):
            mp[num] = i
        for i, num in enumerate(nums):
            diff = target - num
            if diff in mp and i != mp[diff]:
                first = min(i, mp[diff])
                second = max(i, mp[diff])
                return [first, second]

