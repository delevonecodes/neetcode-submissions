class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        majority = [nums[0], 0]

        for num in nums:
            if num != majority[0] and majority[1] >= 1:
                majority[1] -= 1
                if majority[1] == 0:
                    majority[0] = num
            elif num != majority[0]:
                majority[0] = num
            elif majority[0] == num:
                majority[1] += 1
        return majority[0] 
