def square(x):
    return x*x

_list = [1,2,3,4,5,6,7,8]
_lookup_list = [2,2,2,2,2,2,2]
_square_list = []

for i in _list:
    _square_list.append(square(i))
print(_square_list)
_square_list.clear()
print(_square_list)

# With Lambda
_sq = lambda x:x*x
for i in _list:
    _square_list.append(_sq(i))
print(_square_list)
_square_list.clear()
print(_square_list)

#-> map() with Lambda
# map( func,*iterable(s) )

#example 1

print(list(map( lambda x:x+1 ,_list))) 

print(list(map( square ,_list))) 

print(list(map(lambda x,y:x-y,_list,_lookup_list))) 


#-> filter(function, iterable)

print(list(filter(lambda x:x>4,_list)))

#-> zip() this create a list of tuple

print(list(zip(_list,_lookup_list)))

