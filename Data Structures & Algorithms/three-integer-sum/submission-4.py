class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)

        for i, num in enumerate(nums):
            compliment = 0 - num
            l = i+1
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == compliment:
                    if [num, nums[l], nums[r]] not in output:
                        output.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r:
                        total = nums[l] + nums[r]
                        if total == compliment:
                            if [num, nums[l], nums[r]] not in output:
                                output.append([num, nums[l], nums[r]])
                            break
                        elif total > compliment:
                            r -= 1
                        elif total < compliment:
                            l += 1        
                elif total > compliment:
                    r -= 1
                elif total < compliment:
                    l += 1

        return output            
            