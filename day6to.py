#user defined function in python day -6

# def my_function():
#     print("hello from user defind function : ")

# i =0
# while(i<20):
#     my_function()
#     i = i+1


# que - making a result of a student
def contact():
    print("contact detail of the school:")
    print("Delhi public school")
    print("Bangolore karanatka")
    print("8815750023669")
    print("dps.contact@gmail.com")


for i in range(4):
    name = input("enter the name of the student: ")
    maths = int(input("enter the marks of maths: "))
    phy = int(input("enter the marks of  physics: "))
    che = int(input("enter the marks of che: "))
    eng = int(input("enter the marks of eng:" ))
    percentage = (maths + phy + che + eng)/4
    print("Name of student is : ", name)
    print("maths marks:" , maths)
    print("phy marks:" , phy)
    print("che marks:" , che)
    print("eng marks:" , eng)
    print("result of student is : ", percentage)
    
    print()
    contact()
    print()

