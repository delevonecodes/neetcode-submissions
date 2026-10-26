class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        l, r = 0, len(numbers)- 1
        while l < r:
            sm = numbers[l]+numbers[r]
            if target - sm == 0:
                return [l+1, r+1]
            elif target - sm < 0:
                r -= 1
            elif target - sm > 0:
                l += 1