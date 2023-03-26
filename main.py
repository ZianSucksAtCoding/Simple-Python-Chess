# import required module
import chess
 
# create board object
board = chess.Board()

#1 is white and 0 is black
turn = "white"
 
# display chess board
print(board)

while True:
    # moving players
    board.push_san(input("I Would like to play: "))
  
    # Display chess board 
    print(board)
    
    if turn == "white":
        turn = "black"
    else:
        turn = "white"
    
    if turn == "white":
        if board.is_checkmate() == True:
            print("Black Wins By Checkmate!")
            exit()
    else:
        if board.is_checkmate() == True:
            print("White Wins By Checkmate!")  
            exit()
