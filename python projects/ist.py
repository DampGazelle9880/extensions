theboard = {'7': ' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '1':' ','2':' ','3':' '}
board_key = []     
for key in theboard:
    board_key.append(key)
def printBoard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print(board['1']+'|'+board['2']+'|'+board['3'])
def game():
    turn = 'X'
    count = 0
    for i in range(10):
      printBoard(theboard)
      print("It's your turn!", + turn +"Move to which place?") 
      move = input()
      if theboard[move] ==' ':
         theboard[move]=turn
         count += 1
      else:
        print("This place is already filled.\nMove to which place?")
        continue   
      if count>=5:
        if theboard['7']== theboard['8']== theboard['9']!=' ': 
            printBoard(theboard)
            print("\nGame Over!")
            print("***" + turn + "won.***")
        elif theboard ['4']== theboard['5']== theboard['6']!=' ':
            printBoard(theboard)
            print("\nGame Over!")
            print("***" + turn + "won.***")
        elif theboard ['1']== theboard['2']== theboard['3']!=' ':
            printBoard(theboard)
            print("\nGame Over!")
            print("***" + turn + "won.***")
        elif theboard ['1']== theboard['4']== theboard['7']!=' ':
            printBoard(theboard)
            print("\nGame Over!")
            print("***" + turn + "won.***")
        elif theboard ['2']== theboard['5']== theboard['8']!=' ':
            printBoard(theboard)
            print("\nGame Over!")
            print("***" + turn + "won.***")
        elif theboard ['3']== theboard['6']== theboard['9']!=' ':
                printBoard(theboard)
                print("\nGame Over!")
                print("***" + turn + "won.***")
        elif theboard ['7']== theboard['5']== theboard['3']!=' ':
            printBoard(theboard)
            print("\nGame Over!")
            print("***" + turn + "won.***")
        elif theboard ['1']== theboard['5']== theboard['9']!=' ':
            printBoard(theboard)
            print("\nGame Over!")
            print("***" + turn + "won.***")
      if count == 9:
        print("\nGame Over!") 
        print("It's a tie!") 
      if turn == 'X':
        turn = '0'
      else:
        turn = 'X'
    restart = input("Do you want toplay again?y/n") 
    if restart == 'y' or restart == 'Y':
      for key in board_key:
        theboard[key]=" "
      game()
if __name == "__main__":
    game()                              
                             

    
           
            