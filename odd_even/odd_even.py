print("Welcome to our Programme.\n")

number = input("Now input a number between 1 and 1000: ")

try:
    number1 = int(number)
except:
    number1 = -1

number2 = 0

try:
    if number1 <= 1000:
        number2 = number1
except:
    number2 = -1

if number2 > 0:
    if (number2 % 2 == 0):
        print("That's an even number!")
    else:
        print("That's an odd number!")
else:
    print("Something is wrong! You have to input a number between 1 and 1000.")
