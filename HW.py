import random
import string

print("Hello, Welcome to Password generator!")

length = int(input("\nEnter the length of password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits

symbols = string.punctuation 

#string.ascii_letters

all = lower + upper + num + symbols

temp = random.sample(all, length)

password = "".join(temp)
print(password)