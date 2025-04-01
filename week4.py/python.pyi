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