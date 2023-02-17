list1=[2,"hello",1.1,True,]
print(list1)
list2 = [1,2,3,4,5,6,77]
print(sum(list2))        #returns sum of list values
print(max(list2))        #returns the maximum values
print(min(list2))        #returns the minmum value
print(sorted(list2))
print(list1.count(2))        #returns the number of elements with the specified value
list2.append(77)
print("append",list2)     #adds an element at the end of the list
list2.reverse()
print("reverse",list2)     # reverses the order of the list
list2.pop()
print("pop" ,list2)        #last value from the list or the given index value 
list2.copy()
print("copy",list2)       #returns a copy of the list
list2.sort()
print("sort",list2)       # sorts the list
list2.remove(77)
print("sort",list2)
list2.remove(77)
print("remove",list2)       #remove the first item with the specified value
list2.insert(3,88)
print("insert",list2)        #insert a given element at a given index in a list 
sl = list2[::-1]
print(sl)
print("h==",list2.index(88))
sl = list2[0:1]
print(sl)
sl = list2[0:4]
print(sl)
print("index",list2.index(88))        # returns the index of the first el
print(type(list2))
list2.extend(list1)                     # iterable to the end of the list
print(list2)
print(len(list2) )                     #returns the length
print(list2.count(7)) 
print(list2.clear())             #removes all the elements from the list