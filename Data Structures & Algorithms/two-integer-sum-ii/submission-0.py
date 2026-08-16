class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            dist = target - (numbers[l] + numbers[r])
            if dist == 0:
                return [l + 1, r + 1]
            elif dist < 0:
                r -= 1
            elif dist > 0:
                l += 1
            
