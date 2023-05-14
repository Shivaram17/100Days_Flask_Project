class Solution:
    # 3 x 3 grid method
    def loop_short(self,n,m, board):
        print('I am loop_short:')
        for i in range(n,m):
            d = {}
            for j in range(3):
                if board[i][j] != '.':
                    if board[i][j] in d.keys():
                        return 'false'
                    else:
                        d[board[i][j]] = 1

        for i in range(n,m):
            d = {}
            for j in range(3,6):    
                if board[i][j] != '.':
                    if board[i][j] in d.keys():
                        return 'false'
                    else:
                        d[board[i][j]] = 1
        for i in range(n,m): 
            d = {}
            for j in range(6,9):    
                if board[i][j] != '.':
                    if board[i][j] in d.keys():
                        return 'false'
                    else:
                        d[board[i][j]] = 1

        return 'true'
    def isValidSudoku(self, board):
        #i Iterating row wise
        for input in board:
            d = {}
            for j in input:
                if j != '.':
                    if j in d.keys():
                        return 'false'
                    else:
                        d[j] = 1
            
        #ii iterating column wise
        for i in range(9):
            d = {}
            for item in board:
                # checking if the first element is in the dictionary
                if item[i] != '.':
                    if item[i] in d.keys():
                        return 'false'
                    else:
                        d[item[i]] = 1

        level_1 = self.loop_short(0, 3, board)
        level_2 = self.loop_short(3, 6, board)
        level_3 = self.loop_short(6, 9, board)

        # print(level_1, level_2, level_3)
        # check if any of the levels are False
        if not ((level_1 and level_2) and level_3):
            return 'false'

        return 'true'

board_list = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
obj = Solution()
obj.isValidSudoku(board_list)
