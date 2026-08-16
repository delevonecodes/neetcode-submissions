class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        sl = sorted([num for num in counter],key=lambda num: counter[num], reverse = True)
        return sl[:k]



