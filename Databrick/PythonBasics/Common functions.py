from collections import Counter

#Count, counter, isinstance, isdigit, ord

print('----------------Count vs Counter------------------')

_str = "thisthisok"
_lst = [1,2,3,4,5,1,2,]

print( _str.count('t') )  #only accept string argument

print( dict(Counter(_str) )) # can accept str and sequence objects
print( dict(Counter(_lst) ))


print("-------------------Instance----------------------")

# checks if objects datatypes-> int float str bool list dict

print( isinstance(_str, str ) )
print( isinstance(_str, float) )
print( isinstance(_lst, list) )
print( isinstance( {3:'3'} , dict) )


print("-------------------isdigit----------------------")
_str1 = '1234'
_str2 = '123 5' # technically this could not be a digit 

print(_str1.isdigit())
print(_str2.isdigit())

print("-------------------ord----------------------")

# each character has its own unicode in 
print(ord('A'), ord('Z'))  # Output: 65-90 (Unicode for 'A')
print(ord('a'), ord('z'))  # Output: 97-122(Unicode for 'a')
print(ord('0'), ord('9'))  # Output: 48-57 (Unicode for 'a')

