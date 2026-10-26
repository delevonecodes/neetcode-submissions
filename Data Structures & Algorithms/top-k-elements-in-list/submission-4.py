class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        counts = [[] for i in range(len(nums)+1)]
        mp = {}
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        for num, freq in mp.items():
            counts[freq].append(num)
        i = len(counts) - 1
        output = []
        while k:
            j = len(counts[i]) - 1
            while k and counts[i]:
                output.append(counts[i][j])
                counts[i].pop()
                j-=1
                k-=1
            i-=1
        return output
        


        
        
        
            


        