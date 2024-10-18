camel_case= input("Please enter the name of the variable in camel case: ")
for i in camel_case:
    if i.islower():
     print(i, end="")
    if i.isupper():
        print ("_",i.lower(), end="")
print()