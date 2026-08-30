class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        rows = []
        columns = []
        boxes = []
        for _ in range(9):
            rows.append(set())
            columns.append(set())
            boxes.append(set())
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                box_num = c//3 + 3*(r//3)
                if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in boxes[box_num]:
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                boxes[box_num].add(board[r][c])
        return True
                                    
        