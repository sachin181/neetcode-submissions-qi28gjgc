class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Checks each row
        for i in range(9):
            hashset = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in hashset:
                    return False
                hashset.add(board[i][j])
        
        #Check each column
        for j in range(9):
            hashset = set()
            for i in range(9):
                if board[i][j] != "." and board[i][j] in hashset:
                    return False
                hashset.add(board[i][j])
        
        for r_start in range (0, 9, 3):
            for c_start in range (0, 9, 3):
                hashset = set()
                for i in range (r_start, r_start + 3):
                    for j in range (c_start, c_start + 3):
                        if board[i][j] != "." and board[i][j] in hashset:
                            return False
                        hashset.add(board[i][j])

        return True


                  
        