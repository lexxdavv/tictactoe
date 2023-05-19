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


# TODO: create row_2 and row_3 and put into printed grid
row_1 = ['A', 'B', 'C']


print(f"{row_1[0]}|{row_1[1]}|{row_1[2]}")
print("-----")
print(" | | ")
print("-----")
print(" | | ")


