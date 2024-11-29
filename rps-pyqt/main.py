import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class TTCWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Tic Tac Toe")
        layout = QtWidgets.QGridLayout(self)
        
        self.player_turn = QtWidgets.QLabel(f"Player turn: {player_turn}")
        self.turn_count = QtWidgets.QLabel(f"Turn count: {turn_count}")
        
        
        
        self.upper_left = QtWidgets.QPushButton("")
        self.upper_middle = QtWidgets.QPushButton("")
        self.upper_right = QtWidgets.QPushButton("")
        
        self.center_left = QtWidgets.QPushButton("")
        self.center_middle = QtWidgets.QPushButton("")
        self.center_right = QtWidgets.QPushButton("")
        
        self.bottom_left = QtWidgets.QPushButton("")
        self.bottom_middle = QtWidgets.QPushButton("")
        self.bottom_right = QtWidgets.QPushButton("")
        
        layout.addWidget(self.player_turn)
        layout.addWidget(self.turn_count)
        
        layout.addWidget(self.upper_left, 0, 0)
        layout.addWidget(self.upper_middle, 0, 1)
        layout.addWidget(self.upper_right, 0, 2)
        
        layout.addWidget(self.center_left, 1, 0)
        layout.addWidget(self.center_middle, 1, 1)
        layout.addWidget(self.center_right, 1, 2)
        
        layout.addWidget(self.bottom_left, 2, 0)
        layout.addWidget(self.bottom_middle, 2, 1)
        layout.addWidget(self.bottom_right, 2, 2)
        



"""
BASE Tic-Tac-Toe-Game [stops after check_win() == True or turn_count == 9]
"""

player_turn = "X"
turn_count = 0


X_player_win = 0
O_player_win = 0

board = [[".", ".", "."], 
         [".", ".", "."], 
         [".", ".", "."]]


def display_board(board):
    global player_turn
    global turn_count
    
    global X_player_win
    global O_player_win
    
    print(f"X Wins: {X_player_win}")
    print(f"O Wins: {O_player_win}\n")

    print("Player Turn:", player_turn)
    print("Turn Count:", turn_count)
    for line in board:
        print(str(line) + "\n")
        
def proceed_turn():
    global board
    global player_turn
    global turn_count
    
    match player_turn:
        case "O":
            player_turn = "X";
        case "X":
            player_turn = "O";
        case _:
            player_turn = "X";
                
    turn_count+=1
    
    
    
def check_vertical():
    global board
    global X_player_win
    global O_player_win
    
    global player_turn
    
    for col in range(0, 3):
        if (board [0][col] == player_turn) and (board [1][col] == player_turn) and (board [2][col] == player_turn):
            return True
        
def check_horizontal():
    global board
    global X_player_win
    global O_player_win
    
    global player_turn
    
    for row in range(0, 3):
        if (board [row][0] == player_turn) and (board [row][1] == player_turn) and (board [row][2] == player_turn):
            return True 
        
def check_diagonal():
    global board
    global X_player_win
    global O_player_win
        
    global player_turn
        
    if (board[1][1] == player_turn):
        if(board[0][0] == player_turn) and (board[2][2] == player_turn):
            return True
        elif(board[0][2] == player_turn) and (board[2][0] == player_turn):
            return True    
                
def check_win():
    global board
    global X_player_win
    global O_player_win
    
    global player_turn
    global win_game
    
    if (check_horizontal() == True) or (check_vertical() == True) or (check_diagonal() == True):
        if player_turn == "X":
            X_player_win +=1
        elif player_turn == "O":
            O_player_win +=1
            
        print(display_board(board))
        print(f"{player_turn} wins!")
        return True
    return False
            
            

def test_function():
    for turn in range(0, 3):
        row = int(input(f"Choose where you want to place an {player_turn} horizontally: "))
        col = int(input(f"Choose where you want to place an {player_turn} vertically: "))

        board[row][col] = player_turn
        
        if check_win() == True:
            return "Test complete. Check works!"
    return "Test failed!"



def play_game():
    global board
    global X_player_win
    global O_player_win
    
    global player_turn
    
    while turn_count < 9:
        display_board(board)
        row = int(input(f"Choose where you want to place an {player_turn} horizontally: "))
        col = int(input(f"Choose where you want to place an {player_turn} vertically: "))
        
        if board[row][col] != "X" and board[row][col] != "O":
            board[row][col] = player_turn
            if check_win() == True:
                break
            else:
                proceed_turn()
        else:
            continue
        
    if turn_count == 9:
        print("GAME TIED")
    
app = QtWidgets.QApplication([])

widget = TTCWidget()
widget.resize(800, 600)
widget.show()

sys.exit(app.exec())
    

    



    
    
    
    

    



    
    
    
