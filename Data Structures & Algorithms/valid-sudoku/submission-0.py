class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        line = [[],[],[],[],[],[],[],[],[]]
        column = [[],[],[],[],[],[],[],[],[]]
        squares = [[[],[],[]],[[],[],[]],[[],[],[]]]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                num = int(board[i][j])

                if num in line[i]:
                    return False
                else:
                    line[i].append(num)

                if num in column[j]:
                    return False
                else:
                    column[j].append(num)

                if num in squares[i//3][j//3]:
                    return False
                else: 
                    squares[i//3][j//3].append(num)

        return True
