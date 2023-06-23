#HELPFUL COMMENTS

#-comment more than one line cmnd(alt) + /
#-another way is triple single quotes ''' before and after block of texts ex below
'''this is
an example
print("hello world")'''
#-cmnd + k = clears terminal
#-TTT = tictactoe

#---------------------------------------------------------------------------------------------

# print("|_____|_____|_____|")
# print("-------------------")
# print("|_____|_____|_____|")
#this is how i first decided to do the TTT board

#---------------------------------------------------------------------------------------------

# letters = str(input("Enter 7 puzzle letters: ")) # input from player
# print("--------SPELLING BEE-------") # lines 4-15 prints beehive and letter indexes
# print("--------- / ¯¯¯ \ ---------")
# print("---------    " + letters[2].upper()+ "    ---------")
# print("----/ ¯¯¯ \ ___ / ¯¯¯ \----")
# print("----   " + letters[3].upper()+ "           " + letters[1].upper()+ "   ----")
# print("----\ ___ / ¯¯¯ \ ___ /----")
# print("---------    " + letters[0].upper()+ "    ---------")
# print("----/ ¯¯¯ \ ___ / ¯¯¯ \----")
# print("----   " + letters[4].upper()+ "           " + letters[6].upper()+ "   ----")
# print("----\ ___ / ¯¯¯ \ ___ /----")
# print("---------    " + letters[5].upper()+ "    ---------")
# print("--------- \ ___ / ---------")
#used this code from cs111 as references to get an idea of how the TTT board could be printed

#---------------------------------------------------------------------------------------------

# TODO: do first. create row_2 and row_3 and put into printed grid
# TODO: do second. use the input function to fill out some spaces on the grid
# TODO: do third. add input validation. for example, only allow empty spaces to be input
# TODO: do fourth. keep prompting for input
# TODO: checks for only empty spaces
# TODO: switching between X & O's
# TODO: input saying whose turn it is
# TODO: determine when someone wins & print winner
# TODO: if no one has won after n turns (n=9), then declare tie
# TODO: push to github when finished
# TODO: down the line tic-tac-toe vs computer
# pretend tic tac toe board is a grid. 0,0 is the upper left. 2,2 is the bottom right.
# response = input('Which space do you want to fill with an X?:')

# row_1 = ['A', 'B', 'C']
# row_2 = ['1', '2', '3']
# row_3 = ['X', 'Y', 'Z']


row_1 = [' ', ' ', ' ']
row_2 = [' ', ' ', ' ']
row_3 = [' ', ' ', ' ']

def board():
    print(f"{row_1[0]}|{row_1[1]}|{row_1[2]}")
    print("-----")
    print(f"{row_2[0]}|{row_2[1]}|{row_2[2]}")
    print("-----")
    print(f"{row_3[0]}|{row_3[1]}|{row_3[2]}")
#board()

gameover = False
while not gameover:
    response = input('Which space do you want to fill with an X?:')

    if response == '0,0' and row_1[0] == ' ':
        row_1[0] = 'X'
        board()
    elif response == '0,1' and row_1[1] == ' ':
        row_1[1] = 'X'
        board()
    elif response == '0,2' and row_1[2] == ' ':
        row_1[2] = 'X'
        board()
    elif response == '1,0' and row_2[0] == ' ':
        row_2[0] = 'X'
        board()
    elif response == '1,1' and row_2[1] == ' ':
        row_2[1] = 'X'
        board()
    elif response == '1,2' and row_2[2] == ' ':
        row_2[2] = 'X'
        board()
    elif response == '2,0' and row_3[0] == ' ':
        row_3[0] = 'X'
        board()
    elif response == '2,1' and row_3[1] == ' ':
        row_3[1] = 'X'
        board()
    elif response == '2,2' and row_3[2] == ' ':
        row_3[2] = 'X'
        board()
    else:
        print('Invalid move! Please pick a new space!')