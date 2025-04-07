def directions(): #First function
    steps=["Move Forward","Move Backward","Turn Left","Turn Right"]
    return steps

def menu_and_input(): #Second Function
    print("Please Select a direction")
    dir=directions()
    for index in range(len(dir)):
        print(dir)
        print(dir[1])
menu_and_input()


def menu_and_input(): #Second Function
    print("Please Select a direction")
    dir=directions()
    for index in range(len(dir)):
        print(index,dir[index])
        print(dir[1])
menu_and_input()


def menu_and_input():  # Third Function
    print("Please Select a direction")
    dir = directions()
    for index in range(len(dir)):
        print(index, dir[index])
    user_choice = int(input())
    return dir[user_choice]


menu_and_input()

def run_task4():
  route=[]