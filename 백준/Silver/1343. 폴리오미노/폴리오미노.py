import sys 
input = sys.stdin.readline 

board = input()
board_1 = board.replace('XXXX',"AAAA")
board_2 = board_1.replace('XX','BB')

if 'X' in board_2:
    print(-1) 
else:
    print(board_2)