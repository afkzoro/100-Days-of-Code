import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

rand_let = random.choices(letters, k=nr_letters)
rand_num = random.choices(numbers, k=nr_numbers)
rand_sym = random.choices(symbols, k=nr_symbols)

new_list = []
new_list.append(rand_let)
new_list.append(rand_num)
new_list.append(rand_sym)


flat_list = new_list[0] + new_list[1] + new_list[2]
#print(flat_list)
length = len(flat_list)
#print(length)

new_pass = ''
passwd  = random.sample(flat_list, length)
for x in passwd:
 new_pass += x
print(new_pass)
 