import random

# initialise all necessarry values
points = 0
misses = 0
i = 10

# run while loop for game
while i != 0:
    number1 = random.randint(2,10)
    number2 = random.randint(2,10)
    print(number1,"x",number2)
    right1 = (number1 * number2)
    
    solution = input("How's the solution? (Enter for a new Task): ")
    if solution != "":
        if number1 * number2 == solution:
            print("That's right!")
            points = points + 1
        else:
            print("That's wrong! ",richtig1,"would be right")
            misses = misses + 1
        i -= 1

# print out result
print("You got",points,"Tasks right and",misses,"misses")
