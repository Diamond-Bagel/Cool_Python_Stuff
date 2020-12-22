import math

# For example later on
class Thing:
  def __init__(self):
      print('thing')
obj = Thing()

def foo():
    return math.pi*(4**2)

# The type() function can return a variety of things 
print(type(1))                        # returns 'int'
print(type(1.0))                      # returns 'float'
print(type('1'))                      # returns 'string'
print(type([1]))                      # returns 'list'
print(type({'1': 1}))                 # returns 'dict'
print(type({1}))                      # returns 'set'
print(type(True))                     # returns 'bool'
print(type(None))                     # returns 'NoneType'
print(type(print))                    # returns 'builtin_function_or_method'
print(type(print()))                  # returns 'NoneType'
print(type(math))                     # returns 'module'
pritn(type(thing))                    # returns 'type'

# using type() on called functions returns what said function returns
print(type(foo())                     # returns 'float'

# These return '__main__.(class_name)'
print(type(thing()))                  # returns '__main__.thing'
print(type(obj))                      # returns '__main__.thing'

# Opening files
f = open('file.txt', 'w')
print(type(f))                        # returns 'io.TextIOWrapper'  (returned for all file types)
print(type(f.write("function")))      # returns 'int'   (idk why)
f.close()