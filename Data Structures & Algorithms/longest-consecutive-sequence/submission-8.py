class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hset = set(nums)
        max_seq = 1
        for i in range(len(nums)):
            if nums[i] - 1 not in hset:
                running_seq = 1
                curr_numb = nums[i]
                while curr_numb + 1 in hset:
                    curr_numb += 1
                    running_seq += 1
                max_seq = max(max_seq, running_seq)
        return max_seq