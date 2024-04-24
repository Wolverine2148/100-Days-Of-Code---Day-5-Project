#Password Generator Project
import random
# I'm guessing you know what this is
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Asking the user how many of 
# each character do they want
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for letter in range(1, nr_letters + 1):
#   password += letters[random.randint(1, len(letters) - 1)]
# for number in range(1, nr_numbers + 1):
#   password += numbers[random.randint(1, len(numbers) - 1)]
# for letter in range(1, nr_letters + 1):
#   password += symbols[random.randint(1, len(symbols) - 1)]
# print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#Save password as list
password = []
#Adding random letters , numbers and symbols 
for letter in range(1, nr_letters + 1):
  password.append(letters[random.randint(1, len(letters) - 1)])
for number in range(1, nr_numbers + 1):
  password.append(numbers[random.randint(1, len(numbers) - 1)])
for letter in range(1, nr_letters + 1):
  password.append(symbols[random.randint(1, len(symbols) - 1)])
#Shuffling the order of the list(To randomise)
random.shuffle(password)
#Turning the list into a string by 
#Individually adding each character
#from the list into the string
#using a for loop
passwo = ""
for i in password:
  passwo += i
#showing the user their password
print(f"You password is {passwo}")
