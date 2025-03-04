number1 = int(input("Enter the number"))

def oddoreven():

    if number1%2==0:
        print(f"The number{number1} is even")
    else:
        print(f"Your number{number1} is odd")

oddoreven()

def multipleof5():
    if number1/5==0:
        print(f"The {number1} is divided by 5")
    else:
        print(f"The {number1} is not divided by 5")

multipleof5()

def addfunction():
    num1=int(input("enter 1number"))
    num2=int(input("enter 2number"))
    num3=int(input("enter 3number"))
    num4=int(input("enter 4number"))
    num5=int(input("enter 5number"))
    sum=num1+num2+num3+num4+num5
    print(f"the total of 5numbers{sum}")
addfunction()