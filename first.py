print("hello world in python..........")

# variable in python  day -2
x = 10
y= 15.3
z = "bhagwan singh rana"
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))


#data types in python day -2
# numeric 
# dictionary
# tuples
# list 
# set 
# boolean
# strings

x = 10
y= 15.3
z = "bhagwan singh rana"
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

x = (2,3,56,986,58)
print(x)
print(type(x))

list = [1,5,8,6,9,3,5,7]
print(list)
print(type(list))



# operators in python day -2
 
a =20
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a>b)
print(a<b)

print(a and b)
print(a or b)
print(not(a))



# types of function in python day -3
#build in function or inbuilt function
x= abs(-5.99)
print(x)
a = abs(3 +5j)
print(a)

z= bin(13)
print(z)
l = bin(5)
print(l)

b = bytes(4)
print(b)

c = chr(97)
print(c)
c1 = chr(98)
print(c1)

cl = complex(3.5)
print(c1)

f= float(3)
print(f)

i= int(12.256)
print(i)


f= float(3)
print(f)

i= int(12.256)
print(i)


#control flow statement in python day -4
age = 25
if (age>=18):
     print("you are eligible for vote ")

a =int(input("enter a number .........."))
if a>=90:
     print("A Grade ")
if a>=75 and a<90:
     print("B grade")
if a>=65 and a< 75:
     print("C GRADE")
if a<65:
     print("fail ")


#que-- accept the city and print and monument
city = input("enter the city   : ")
if city=='delhi':
     print("Red Fort")
elif city=='agra':
     print("Taj mahal")
elif city=='jaipur':
     print("JaiMahal")
elif city=='orissa':
     print("Konak temple")
elif city=='hyderabad':
     print("charminar")
else:
     print("record not found ")


#loops in python day - 5
i= 1
n =2000
while(i<=n):
     print("hello world ")
     i = i+10



num = int(input("enter the number :"))
i =1
while(i<=10):
     print(num," * ",i," = ", num*i)
     i= i+1




#while-else
count = int(input("enter the number :"))
while(count<25):
     count+=1
     print("hello students :")
else:
     print("count is less than 25 :")


#for loop
fruits =["apple", "mongo","banana", "cherry"]
for x in fruits:
     print(x)


for x in range(3,25):     # 25 in not include in condition
     print(x)