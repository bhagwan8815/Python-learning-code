#string in python

str = "welcome to the python class of string :"
print(str)

str1 = '''My name is bhagwan
singh rana, i am a student of mit college .
i want to become a softwate engineer.
i have knowledge of java , python , react, mongodb, node js '''
print(str1)


# indexing in string 
 # H  E  L  L  O
 # 0  1  2  3  4
 #-5 -4 -3 -2 -1

str2 = "Jay Shree mahakal"
print(str2[2])  # y
print(str2[3])  # space
print(str2[5])  # h
print(str2[-1]) # l
print(str2[-7]) # m
print(str2[-8]) # space



# slicing of string str[start:end:skip]
str3 = "hello student how are you"
print(str3[0:5]) # hello , here 5 is length.
print(str3[::2])  #hlosuethwaeyu   
print(str3[6:18])


#reverse  string in python
str4 = "hello students"
print(str4[::-1])

#how to find length of string 
print(len(str4))

#upper method 
print(str4.upper())



#lower method
str5="JAY SHREE MAHAKAL "
print(str5.lower())

#replace method
a="hello how are you"
print(a.replace("hello","bye"))

#find method 
a ="python is grate"
print(a.find("g"))  #10