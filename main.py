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
# declare tie
# ask does player want to play alone with ai or with a person
# make sure if the player who wins wants to play again they start first     
# if statements and print board before each game for new games

# row_1 = ['A', 'B', 'C']
# row_2 = ['1', '2', '3']
# row_3 = ['X', 'Y', 'Z']


#cur_player = ''

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

#counting up to the number of possible turns which is 9, counter starts @ 0 bc no one has taken a turn, so after the first turn it counts up until the last turn
counter = 0

#allow players to keep playing until gameover = True/all 9 turns are fulfilled (will change if someone wins b4 9 turns)
gameover = False

#while gameover is not true, current player is blank, x's turn bc counter is 0 or divisible by 2(bc any num divisible by 2 doesnt have remainder & remainder of 2 has to == 0), if not then it will be o's turn
#asking: is gameover false? yes, it is false so we enter the loop.
while not gameover:
    #cur_player = ''
    if counter == 0 or counter % 2 == 0:
        cur_player = 'X'
    else:
        cur_player = 'O'

#prints whose turn it is and asks for input
    print(f"Player {cur_player} turn.")
    response = input('Which space do you want to fill with an ' + cur_player + '?:')




#look into global...good or bad? when is it good or bad to use?
    def restart():
        global gameover
        #play_again = ""
        while gameover:
            play_again = input("Gameover! Do you want to play again? Y or N: ")
            if play_again == "Y":
                gameover = False
                counter = 0
                
                board()
            if play_again == "N":
                gameover = True
                print("Thanks for playing!")
                exit()
        #restart()






# allows player X to take their turn
    if response == '0,0' and row_1[0] == ' ':
        row_1[0] = 'X'
        board()
        cur_player = 'O'
    elif response == '0,1' and row_1[1] == ' ':
        row_1[1] = 'X'
        board()
        cur_player = 'O'
    elif response == '0,2' and row_1[2] == ' ':
        row_1[2] = 'X'
        board()
        cur_player = 'O'
    elif response == '1,0' and row_2[0] == ' ':
        row_2[0] = 'X'
        board()
        cur_player = 'O'
    elif response == '1,1' and row_2[1] == ' ':
        row_2[1] = 'X'
        board()
        cur_player = 'O'
    elif response == '1,2' and row_2[2] == ' ':
        row_2[2] = 'X'
        board()
        cur_player = 'O'
    elif response == '2,0' and row_3[0] == ' ':
        row_3[0] = 'X'
        board()
        cur_player = 'O'
    elif response == '2,1' and row_3[1] == ' ':
        row_3[1] = 'X'
        board()
        cur_player = 'O'
    elif response == '2,2' and row_3[2] == ' ':
        row_3[2] = 'X'
        board()
        cur_player = 'O'
    else:
        print('Invalid move! Please pick a new space!')
        continue

# check for winning condition for player X
    if row_1[0] == 'X' and row_1[1] =='X' and row_1[2] == 'X':
        gameover = True
        print("Winner is X")
        #exit()
        restart()
    elif row_1[0] == 'X' and row_2[0] == 'X' and row_3[0] == 'X':
        gameover = True
        print("Winner is X")
        #exit()
        restart()
    elif row_1[1] == 'X' and row_2[1] == 'X' and row_3[1] == 'X':
        gameover = True
        print("Winner is X")
        #exit()
        restart()
    elif row_1[2] == 'X' and row_2[2] == 'X' and row_3[2] == 'X':
        gameover = True
        print("Winner is X")
        #exit()
        restart()
    elif row_2[0] == 'X' and row_2[1] == 'X' and row_2[2] == 'X':
        gameover = True
        print("Winner is X")
        #exit()
        restart()
    elif row_3[0] == 'X' and row_3[1] == 'X' and row_3[2] == 'X':
        gameover = True
        print("Winner is X")
        #exit()
        restart()
    elif row_1[0] == 'X' and row_2[1] == 'X' and row_3[2] == 'X':
        gameover = True
        print("Winner is X")
        #exit()
        restart()
    elif row_1[2] == 'X' and row_2[1] == 'X' and row_3[0] == 'X':
        gameover = True
        print("Winner is X")
        #exit()
        restart()
# prints player X or O turn and asks user what space they want to fill with X/O
    print(f"Player {cur_player} turn.")
    response = input('Which space do you want to fill with an ' + cur_player + '?:')

# allows player O to take their turn
    if response == '0,0' and row_1[0] == ' ':
        row_1[0] = 'O'
        board()
        cur_player = 'X'
    elif response == '0,1' and row_1[1] == ' ':
        row_1[1] = 'O'
        board()
        cur_player = 'X'
    elif response == '0,2' and row_1[2] == ' ':
        row_1[2] = 'O'
        board()
        cur_player = 'X'
    elif response == '1,0' and row_2[0] == ' ':
        row_2[0] = 'O'
        board()
        cur_player = 'X'
    elif response == '1,1' and row_2[1] == ' ':
        row_2[1] = 'O'
        board()
        cur_player = 'X'
    elif response == '1,2' and row_2[2] == ' ':
        row_2[2] = 'O'
        board()
        cur_player = 'X'
    elif response == '2,0' and row_3[0] == ' ':
        row_3[0] = 'O'
        board()
        cur_player = 'X'
    elif response == '2,1' and row_3[1] == ' ':
        row_3[1] = 'O'
        board()
        cur_player = 'X'
    elif response == '2,2' and row_3[2] == ' ':
        row_3[2] = 'O'
        board()
        cur_player = 'X'
    else:
        print('Invalid move! Please pick a new space!')
        continue

# check for winning condition for player O
    if row_1[0] == 'O' and row_1[1] =='O' and row_1[2] == 'O':
        gameover = True
        print("Winner is O")
        #exit()
        restart()
    elif row_1[0] == 'O' and row_2[0] == 'O' and row_3[0] == 'O':
        gameover = True
        print("Winner is O")
        #exit()
        restart()
    elif row_1[1] == 'O' and row_2[1] == 'O' and row_3[1] == 'O':
        gameover = True
        print("Winner is O")
        #exit()
        restart()
    elif row_1[2] == 'O' and row_2[2] == 'O' and row_3[2] == 'O':
        gameover = True
        print("Winner is O")
        #exit()
        restart()
    elif row_2[0] == 'O' and row_2[1] == 'O' and row_2[2] == 'O':
        gameover = True
        print("Winner is O")
        #exit()
        restart()
    elif row_3[0] == 'O' and row_3[1] == 'O' and row_3[2] == 'O':
        gameover = True
        print("Winner is O")
        #exit()
        restart()
    elif row_1[0] == 'O' and row_2[1] == 'O' and row_3[2] == 'O':
        gameover = True
        print("Winner is O")
        #exit()
        restart()
    elif row_1[2] == 'O' and row_2[1] == 'O' and row_3[0] == 'O':
        gameover = True
        print("Winner is O")
        #exit()
        restart()
'''        
def restart():
    play_again = ""
    while gameover:
        play_again = input("Gameover! Do you want to play again? Y or N: ")
        if play_again == "Y":
            gameover = False
            counter = 0
            board()
        if play_again == "N":
            gameover = True
            print("Thanks for playing!")
            exit()
restart()
'''