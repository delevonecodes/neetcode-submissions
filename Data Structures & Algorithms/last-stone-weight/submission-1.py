class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if not stones:
            return 0
        sorted_stones = sorted(stones,reverse=True)
        s1, s2 = sorted_stones[0], sorted_stones[1]
        if s1 == s2:
            del sorted_stones[1]
            del sorted_stones[0]
        elif s1 > s2:
            s3 = s1-s2
            del sorted_stones[1]
            sorted_stones[0] = s3
        return self.lastStoneWeight(sorted_stones)
        




        