dict = {"a" :1,"b":3,"c":6}
print(dict.values())          #return the all values of dictionary
print(dict.keys())             #return the all keys of dictionary
dict1 ={"a":8,"f":0,"name":"antim"}
print(dict1)
dict.update(dict1)           # Updates the dictionary with the elements from anather dictionary
print(dict)
dict.setdefault("r",10)     #key is in the dictionary else  insert  the key with a value to the dictionry
print(dict)
print(dict.popitem())        #return and removes the key value  pair from the dictionary
print(dict.pop("c"))         #return  and  removes the element with the given key      
print(dict.items())           #return the list with all dic keys eith values return a view object that   
print(dict.get("b"))         #returns the value for the given key
print(dict.fromkeys(dict))   #creates a dictoinary from the givem sequence
print(dict.fromkeys(dict,1))
print(dict1.copy())          #returns a copy of the dictionary
print(dict1.clear())         #removes all the elements from the dictionary
print(dict1)
print(max(dict))         # returns the largest item in an iterle
print(min(dict))         # returns the smallest item in an iterle
print(len(dict))         # returns the largest item in an iterle
print(any(dict))         #returns true if any item in an iterable objec is true
