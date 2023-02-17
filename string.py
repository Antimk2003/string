print("________It is string__________")
string = "python"
print("string")
print(string[0])     #searches the string for a specified value and returns the position of where it was found
print(string[1:2]) 
print(string[0:])
print(string[2])
print(len(string))
print(sorted(string))                
print(string[-1])
print(type(string))                
print(string.count("t"))           #Returns the number of times a specified value occurs in a string 
print(string.endswith("th"))      #returns true if the string ends with the specified value
print(string.endswith("f"))
print(all(string))
print(string.capitalize())        #Converts the first character to upper case
print(string.replace("python","java"))      #returns a string where a specified value is replaced with a specified value
x = string.lower()
print(x)                               #Converts a string into lower case
print(string.upper())            #converts a string into  upper case