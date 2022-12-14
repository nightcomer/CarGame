command = ""
stopped = True
while command != "quit":
    command = input(">").lower()
    if command == "help":
        print("""
start - to start car
stop - to stop car
quit - to exit
        """)
    elif command == "start":
        if stopped == True:
            print("car started!")
            stopped = False
        else:
            stopped = False
            print("the car is already running...")
    elif command == "stop":
        if stopped == True:
            print("the car is already off...")
        else:
            print("car stopped!")
            stopped = True
    elif command == "quit":
        exit()
    else:
        print("function not recognized")
