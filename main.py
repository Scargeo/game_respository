# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# %%

# user guesses
guess = ""
count = 0
chance = 3
# array of colors
colors = ["red", "yellow", "green", "blue", "violet", "pink", "white", "black"]

# selecting a random number for iteration
i = random.randrange(7)
secrete = colors[i]

# holding condition
while count < chance:
    print(colors)
    print("I have chosen a color from the list, guess the color \n")

    guess = str(input())
    count += 1

    # win or loss
    if guess == secrete:
        print("You got me and you won!")
        break
    else:
        print("Try again")

    if count == chance and guess != secrete:
        exit(1)

print("LEVEL TWO \n")

# %%
# random numbers
num = random.randrange(5)
num1 = random.randrange(10)
num2 = random.randrange(10)

# mathematical calculations
answer = (num * num1) / num2

print("Which number multiplied by ", num1, " and the results divided by ", num2, "will give you ", answer, "\n")
print("Hint: the number is less than 5 \n")
get = int(input())

# condition
while count < chance:
    if get == num:
        print("That is correct!")
        break
    else:
        print("That's incorrect, try again")

print("Level Three \n")

"""f_number = int(input("ENTER"))
mark = len(f_number)

i = 2
while i < mark:
    predicted_results = i.append(0)
    i += 1
    print(predicted_results)
"""
