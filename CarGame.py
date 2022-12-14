while True:
    command = 0
    i = 1
    while command != "quit":
        command = input(">")
        i = i + 1
        if command == "help":
            print("start - to start car")
            print("stop - to stop car")
            print("quit - to exit")
        elif command == "start":
            print("car started!")
            break
        elif command == "stop":
            print("the car is already off...")
        elif command == "quit":
            exit()
        else:
            print("function not recognized")

    i = 1
    while command != "quit":
        command = input(">")
        i = i + 1
        if command == "help":
            print("start - to start car")
            print("stop - to stop car")
            print("quit - to exit")
        elif command == "start":
            print("the car is already running...")
        elif command == "stop":
            print("car stopped!")
            break
        elif command == "quit":
            exit()
        else:
            print("function not recognized")
