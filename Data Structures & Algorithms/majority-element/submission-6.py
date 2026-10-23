class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = [nums[0], 1]
        for num in nums:
            if num == majority[0]:
                majority[1] += 1
            else:
                if majority[1] == 0:
                    majority[0] = num
                    majority[1] = 1
                else:
                    majority[1] -=1

        return majority[0]
