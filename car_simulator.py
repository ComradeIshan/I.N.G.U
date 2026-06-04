command = ""   #1hr 35 min pe hai ek baar phirse dekhna

start = True

while True:
    command = input(">").lower()
    if command == "start":
        print("Car started...")
        if command == "start":
            print("Car already started...")
    elif command == "stop":
        print("Car stopped...")
    elif command == "help":
        print('''
start - car schalu
stop - car ruk gaya
quit - quit ho gaya hai
''')
    elif command == "quit":
        break
    else:
        print("Invalid command")


