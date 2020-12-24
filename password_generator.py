# The string module is very useful
# string.ascii_letters is A-Z and a-z
# string.digits is 0-9
# string.punctuation is everything else except for whitespace characters

def generate_password(length):
    import random, string
    chars = string.ascii_letters + string.punctuation + string.digits
    password = ''.join(random.choice(chars) for x in range(length)) 
    #Uncomment code below if you want the password to be written to a file
    #website = input("What website is this password for?\n")
    #with open('passwords.txt', 'a') as f:
    #    f.write(f'Password for {website}: \t{password}\n')
    #    f.close()
    return password


generate_password(8)
