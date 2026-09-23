class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grids = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
        columns = [set() for _ in range(9)]
        
        for i, row in enumerate(board):
            seen = set()
            for j, num in enumerate(row):
                if num.isdigit() and num in columns[j]:
                    return False
                elif num.isdigit():
                    columns[j].add(num)
                if num.isdigit() and num in seen:
                    return False
                if num.isdigit():
                    seen.add(num)
                if num.isdigit() and num in grids[i//3][j//3]:
                    return False
                elif num.isdigit():
                    grids[i//3][j//3].add(num)
        return True