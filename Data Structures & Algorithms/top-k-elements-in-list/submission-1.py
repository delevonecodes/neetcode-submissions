class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for i in range(len(nums)+1)]
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in freq:
            counts[freq[num]].append(num)

        out = []
        freq_pointer = len(counts) - 1

        while len(out) < k:
            if counts[freq_pointer]:
                j = 0
                while len(out) < k and j < len(counts[freq_pointer]):
                    out.append(counts[freq_pointer][j])
                    j += 1
            freq_pointer -= 1

        return out
        
        
            


        