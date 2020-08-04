class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.checkNeighbor(row, col, word):
                    return True
        return False
    
    def checkNeighbor(self, row, col, word):
        if len(word) == 0:
            return True
        
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS or self.board[row][col] != word[0]:
            return False
        
        res = False
        self.board[row][col] = '*'
        for r_offset, col_offset in [(0,1), (0,-1), (1,0), (-1,0)]:
            res = self.checkNeighbor(row+r_offset, col+col_offset, word[1:])
            
            if res:
                break
                
        self.board[row][col] = word[0]
        
        return res
