if __name__ == '__main__':
    N = int(input())
    List = []
    commands = []
    
    for command in range(N):
        commands.append(input().split())
    
    for command in commands:
        if command[0] == "insert":
            List.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(List)
        elif command[0] == "remove":
            if int(command[1]) in List:
                List.remove(int(command[1]))
        elif command[0] == "append":
            List.append(int(command[1]))
        elif command[0] == "sort":
            List.sort()
        elif command[0] == "pop":
            List.pop()
        elif command[0] == "reverse":
            List.reverse()
    
