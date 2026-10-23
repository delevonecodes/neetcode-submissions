class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_indexes = set()
        for i in range(len(blocks)):
            if blocks[i] == "W":
                white_indexes.add(i)
        count_white = len(white_indexes)
        if len(blocks) == k:
            return count_white
        l, r = 0, k -1
        min_operations = count_white
        while r < len(blocks):
            operations = 0
            for num in white_indexes:
                if l <= num <= r:
                    operations += 1
            min_operations = min(min_operations, operations)

            l+= 1
            r+= 1

        return min_operations
        