import random
print("Welcome to the PyPassword Generator")

#Character lists
letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
symbols = [
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
        '[', ']', '{', '}', '|', '\\', ':', ';', '<', '>', ',', '.', '?', '/',
        '`', '~', '"', "'"
    ]
numbers = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]

#Get input from user how many characters of each group is desired
total_letters = int(input("How many letters would you like in your password: "))
total_symbols = int(input("How many symbols would you like in your password: "))
total_numbers = int(input("How many numbers would you like in your password: "))

#Randomly choose characters from the letters list based on user input and store them in a new list
chosen_letters = []
for i in range(total_letters):
    x = random.choice(letters)
    chosen_letters.append(x)

#Randomly choose characters from the symbols list based on user input and store them in a new list
chosen_symbols = []
for i in range(total_symbols):
    y = random.choice(symbols)
    chosen_symbols.append(y)

#Randomly choose characters from the numbers list based on user input and store them in a new list
chosen_numbers = []
for i in range(total_numbers):
    z = random.choice(numbers)
    chosen_numbers.append(z)

#Concatenate all the characters in a singular list
possible_password = chosen_letters + chosen_symbols + chosen_numbers
#Epty list to store randomized list items
beta_password = []
for i in range(len(possible_password)):
    x = random.choice(possible_password)
    beta_password.append(x)
    possible_password.pop(possible_password.index(x))

#Join all the item of the list in beta password to output a single word
password = "".join(beta_password)
print(f"\nYour password is: {password}")