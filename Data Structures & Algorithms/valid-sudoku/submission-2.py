class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_box = defaultdict(set)

        for row in range(ROWS):
            for col in range(COLS):
                num = board[row][col]

                if num == ".":
                    continue

                if num in rows[row] or num in cols[col] or num in sub_box[(row // 3, col // 3)]:
                    return False
                
                rows[row].add(num)
                cols[col].add(num)
                sub_box[(row // 3, col // 3)].add(num)
        
        return True