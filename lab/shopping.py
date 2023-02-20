number = int(input())
command = int(input())
while True:
    if command!="End":
        current_command=int(command)
        if number - current_command >= 0:
            number -= current_command
        else:
            print("You went in overdraft!")
            break

        command = input()
    else:
        print("You bought everything needed.")
        break
