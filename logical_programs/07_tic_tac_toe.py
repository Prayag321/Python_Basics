    # @Author: Prayag Bhoir
    # @Date: 26-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 26-07-2024
    # @Title : Python program to simulate tic tac toe game
board = ['-','-','-','-','-','-','-','-','-']

def print_board():
    """
  Description:
    This function print the tic tac toe board

  Parameters:
    none

  Returns:
    none
    """
    print('|'+board[0]+'|'+board[1]+'|'+board[2]+'|')
    print('|'+board[3]+'|'+board[4]+'|'+board[5]+'|')
    print('|'+board[6]+'|'+board[7]+'|'+board[8]+'|')

def check(board):
    """
  Description:
    This function check the wining condition

  Parameters:
    board(list):The tic tac toe board

  Returns:
    boolen: ture or false 
  """
    p1='x'
    p2='o'
    if board[0] == board[1] == board[2] == p1 or board[0] == board[1] == board[2] == p2:
        return True
    elif board[3] == board[4] == board[5] == p1 or board[3] == board[4] == board[5] == p2:
        return True
    elif board[6] == board[7] == board[8] == p1 or board[6] == board[7] == board[8] == p2:
        return True
    elif board[0] == board[3] == board[6] == p1 or board[0] == board[3] == board[6] == p2:
        return True
    elif board[1] == board[4] == board[7] == p1 or board[1] == board[4] == board[7] == p2:
        return True
    elif board[2] == board[5] == board[8] == p1 or board[2] == board[5] == board[8] == p2:
        return True
    elif board[0] == board[4] == board[8] == p1 or board[0] == board[4] == board[8] == p2:
        return True
    elif board[2] == board[4] == board[6] == p1 or board[2] == board[4] == board[6] == p2:
        return True
    else: 
        return False
    

def user_input(board):
    """
  Description:
    This function get the input from user

  Parameters:
    board(list):The tic tac toe board

  Returns:
    x(int): user input
    or user_input(board): a recursive call
   """
    x=int(input("Enter the position "))
    if board[x-1] != '-':
        print("Value already exist please enter new value")
        return user_input(board)
    else:
        return x

def main():
    player1=input("Player 1 name : ")
    player2=input("Player 2 name : ")
    print_board()
    for i in range(9):
        if i%2==0:
            print(f"{player1} turn")
            x=user_input(board)
            board[x-1]='x'
            print_board()
            if check(board):
                print(f"{player1} wins")
                break
        else:
            x=user_input(board)
            print(f"{player2} turn")
            board[x-1]='0'
            print_board()
            if check(board):
                print(f"{player2} wins")
                break
    print("Game over")

if __name__=="__main__":
    main()