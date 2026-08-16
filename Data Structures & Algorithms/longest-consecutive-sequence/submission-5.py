class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numset = set(nums)
        max_length = 1
        current_seq = 1
        for num in numset:
            if num - 1 not in numset:
                running_num = num
                while running_num + 1 in numset:
                    current_seq += 1
                    running_num += 1
                if current_seq > max_length:
                    max_length = current_seq 
                current_seq = 1          
        return max_length
