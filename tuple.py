t = (1,2,6,8,9,3,5,3)
print(t)
print(type(t))           #returns the type of  object
print(max(t))            # returns the largest item in an iterle
print(min(t))            # returns the smallest item in an iterle
print(sum(t))            # sums the items of an iterator
print(len(t))           #returns the length of an object 
print(all(t))           #returns True if all items in iterable object are true 
print(any(t))           #returns true if any item in an iterable objec is true
l =["antim","kushwah"]
print(l)
print(type(l))
print(tuple(l))          #return a tuple 
print(type(l))
t = (2)
print(type(t))
t = (2,)
print(type(t))
t = ()
print(type(t))
tup = (6,77,8,99,0,55,33)
print(len(tup))
print(tup.count(99))
print(tup.index(8))
print(tup[-4])
print(sorted(tup))          # returns a sorted list
print(tuple(tup))
a =(1,8,9,0,6,8,9,)
b =("antim","kushwah")
c = a+b
print(c)
a = (88,99,54,0,44,33,11)
print(99 in a)
print(6 in a )              # print to the standard  output device
print(list(a))             #  returns a list
p = slice(2)
print(a[p])                #return the slice object