class checker:
    def __init__(self, color, x,y):
        self.color = color
        self.x = x
        self.y = y
    def __str__(self):
        if self.color == 'black':
            return '⚫'
        if self.color == 'white':
            return '⚪'
    @staticmethod
    def toString(board):
        s = ''
        print(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if( str(type(board[i][j])) == '<class \'int\'>'):
                    s+= ' 0'
                    continue
                s += str(board[i][j])  
            s+= '\n'
        return s
class game:
    @staticmethod
    def legalMoves(board,x,y,color):
        moves = []

        # if(x-1 >= 0 and y-1 >= 0 and (board[x+1][y+1] == '⚪' and board[x+1][y+1] != '⚫')):
        #     moves.append([x+1,y+1])
        # if(x+1 <= 7 and y+1 <= 7 and board[x+1][y+1] != '⚪' and board[x+1][y+1] != '⚫'):
        #     moves.append([x+1,y+1])
        # if(x-1 >= 0 and y-1 >= 0 and board[x+1][y+1] != '⚪' and board[x+1][y+1] != '⚫'):
        #     moves.append([x+1,y+1])

        if(color == 'white'):
            if(x-1 >= 0 and y-1 >= 0 and board[x-1][y-1] != '⚪' and board[x-1][y-1] != '⚫'):
                moves.append([x-1,y-1])
            if(x-1 >= 0 and y+1 <= 7 and board[x-1][y+1] != '⚪' and board[x-1][y+1] != '⚫'):
                moves.append([x-1,y+1])
            if(x+2 <= 7 and y+2 <= 7 and board[x+1][y+1] == '⚫' and (board[x+2][y+2] != '⚫' and board[x+2][y+2] != '⚪')):
               moves.append(['capture',x+2,y+2])
            if(x-2 >= 0 and y+2 <= 7 and board[x-1][y+1] == '⚫' and (board[x-2][y+2] != '⚫' and board[x-2][y+2] != '⚪')):
               moves.append(['capture',x-2,y+2])
        
        return moves

        
        
            

board = [ [i for i in range(8)] for j in range(8)]
for i in range(0,2):
    for j in range(0,8):
        board[i][j] = checker('black',0,0)
for i in range(6,8):
    for j in range(0,8):
        board[i][j] = checker('white',0,0)
print(checker.toString(board))
s = type(1)
print(game.legalMoves(board,6,7,'white'))
print(board[5])
