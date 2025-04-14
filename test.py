#example0
#while not is always asking is (in this case x) condition false ie is x false?
#while is always asking is condition True?
#x is false, line 6 is asking- is x false? since it is false, we enter the loop, and go thru all the conditions until the loop terminated. since it is...we exit the loop and print statement loop finished is executed.
x = not True
while not x:
    print("x is false")
    x = True
    print("hidden message")
    x = False
    print("its back false")
    x = True
print("x is now true, loop finished")
print("----------")

#example1
#x is set to false,  
x = False
while not x:
    print("x is false")
    x = True
print("Loop finished")

#example2
#enter your name, if name is blank (you clicked enter and didnt enter a name), prompt user to enter a name (continue loop until condition is met), when name is entered print ur name is ...
name = input("enter your name: ")

while name == "":
    print("you didnt enter your name")
    name = input("enter your name: ")

print("your name is f{name}")

#example3
#enter ur age, if input is less than 0, print cant be negative, continues in loop to get age since condition is not met, when age is entered and not neg(loop stops), print u are x years old
age = int(input("enter your age: "))

while age < 0:
    print("age cant be negative")
    age = int(input("enter you age: "))

print(f"you are {age} years old")

#example4
#enter food, if input (food) is q, then loop stops and prints okay bye, if food is NOT q, it continues to loop and ask user for food they like, loop will stop if condition is met (input being q and not food)
food = input("enter a food that you like(q to quit): ")

while not food == 'q':
    print(f"you like {food}")
    food = input("enter another food you like(q to quit): ")

print("okay, bye")

#example5
#enter # between 1-10, if num is less than 1 OR greater than 10, print num not valid, then ask for num again, loop will continue to run until condition is met, condition is met if num is greater than 1 & less than 10, one inputted loop will stop and print the number you picked
num = int(input("enter a # between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("enter a # between 1 and 10: "))

print(f"you picked the number {num}")

#example6
#x is (set to) NOT TRUE, while not (is asking): is x false?, since x is false bc its set to NOT TRUE, then we enter the loop, then it print x is false, the next line sets x to true..., this goes back to the while not loop (which is asking is x false?), and since x is now (not false) true, we exit the loop and print loop finished
x = not True
while not x:
    print("x is false")
    x = True
print("x is now true, loop finished")

print("----------")

#example7
#x is set to true, while is asking...is x true? it is, so we enter the loop, and the print statement is executed, we go to the next line which is now set to false...since a new condition is set (x is now false), it goes back to the while x line and validates it...which will ask- is x true. it is not, loop is exited and print statement is executed
x = True
while x:
    print("x is true")
    x = False
print("x is now set to false, we have exited the loop")

#example8
#
