def main ():
    number = int(input())
    dynamic_list(number)

    

def dynamic_list (number):
    user_list = []
    for i in range (0,number):
        command = input().split()
        if command [0].lower() == "insert":
            user_list.insert(int(command[1]),int(command[2]))
        elif command [0].lower() == "print":
            print(user_list)
        elif command [0].lower() == "remove":
            user_list.remove(int(command[1]))
        elif command [0].lower() == "append":
            user_list.append(int(command[1]))
        elif command [0].lower() == "sort":
            user_list.sort()
        elif command [0].lower() == "pop":
            user_list.pop()
        elif command [0].lower() == "reverse":
            user_list.reverse()
        else:
            pass
    return user_list





if __name__ == '__main__':
    main()