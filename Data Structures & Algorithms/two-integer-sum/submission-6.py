class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            num_map[num] = i

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in num_map and i != num_map[compliment]:
                return [i, num_map[compliment]]

