# Classic method
print("Hello world!")

# Using comma(,) operator
print("Hello", "world!")

# Using string concatenation
print("Hello " + "world!")

# Using % substitution
print("%s%s" % ("Hello ", "world!"))

# Using the format method
print("Hello {}".format("world!"))

# Using an f-string
print(f"Hello {'world!'}")

# Using a basic variable
string = "Hello world!"
print(string)

# Printing out value of an array
array = ["Hello world!"]
print(array[0])

# Printing out value of a dictionary
dictionary = {"1": "Hello world!"}
print(dictionary['1'])

# Writing to a file, then reading its contents
with open('hello world.txt', 'r+') as f:
    f.write("Hello world!")
    f.close()
    f = open('hello world.txt', 'r')
    print(f.read())
