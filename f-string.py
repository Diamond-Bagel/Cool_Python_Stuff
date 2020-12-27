# f-strings are quite a useful feature in Python 

# Basic use of an f-string
user_name = input("What is your name?\n").capitalize().strip()
print(f"Hello there, {user_name}.")

# This is quite similar to using .format()

# f-strings automatically type casting
fav_num = 7
print(f"My favorite number is {fav_num}")

# Normally, you would have to do something like this:
fav_num = 8
print("My favorite number is " + str(fav_num))

# Something surprising about f-strings is that you can actually apply boolean logic to them, similar to a lambda function
import random
num_gotten = random.randrange(1, 13)
print(f"The number rolled was {'an' if num_gotten == 11 else 'a'}")
