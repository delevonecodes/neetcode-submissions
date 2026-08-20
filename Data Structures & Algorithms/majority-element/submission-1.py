class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        count = {}
        majority = len(nums) // 2
        for num in nums:
            if num in count and count[num] >= majority:
                return num
            if num in count:
                count[num] += 1
            else:
                count[num] = 1 