set2 = {2,3,4,5,6,7,8,9,10}
print(set2)
set3 = {2,55,66,9,133,99}
print(set3)
print(set2.intersection(set3))      #returns a set , that is the intersection of two or more set
print(set3.union(set2))             #returns a set containing the union of set 
print(set2.difference(set3))        #return a set containing the difference between two or more sets
print(set2.copy())                  #return the copy  of the set
print(set3.pop())                   #remove an element from the set
print(set2.clear())                 #remove all the elementa from the set
print(set2) 
set1 = {"hello","hii","attu"}
print(set1)
print(set1.remove("hello"))          #removes the specified element
print(set1)
set2 = {1,5,2,0,11,7,8}
print(set2)
print(set1.update(set2))            #update the set with another set or any other iterable
print(set1)
print(set2.discard(1))              #remove the specified item
print(set2)
print(set2.copy())                   
print(min(set2))                   # returns the smallest item in an iterle
print(max(set2))                   # returns the largest item in an iterle
print(any(set2))                   #returns true if any item in an iterable objec is true
print(sum(set2))                   # sums the items of an iterator     
print(len(set2))                   #returns the length of an object 