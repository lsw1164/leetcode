class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.is_valid_col(board, i): return False
            if not self.is_valid_row(board, i): return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_valid_subbox(board, i, j): return False
        return True
                
            
        
    def is_valid_subbox(self, board, sr, sc):
        visit = [False]*10
        for r in range(sr, sr+3):
            for c in range(sc, sc+3):
                val = board[r][c]
                if val == '.': continue
                if visit[int(val)]: return False
                visit[int(val)] = True
        return True
    
        
    def is_valid_col(self, board, col_idx):
        visit = [False]*10
        for i in range(9):
            val = board[i][col_idx]
            if val == '.': continue
            if visit[int(val)]: return False
            visit[int(val)] = True
        return True
    
    
    def is_valid_row(self, board, row_idx):
        visit = [False]*10
        for i in range(9):
            val = board[row_idx][i]
            if val == '.': continue
            if visit[int(val)]: return False
            visit[int(val)] = True
        return True
            