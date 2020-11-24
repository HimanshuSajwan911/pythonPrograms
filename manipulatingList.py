if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(0, N):
        task = input().split()
        if "append" in task:
            arr.append(int(task[1]))
        elif "insert" in task:
            arr.insert(int(task[1]), int(task[2]))
        elif "sort" in task:
            arr.sort()
        elif "print" in task:
            print(arr)
            continue
        elif "pop" in task:
            arr.pop()
        elif "reverse" in task:
            arr.reverse()
        elif "remove" in task:
            arr.remove(int(task[1]))
        else:
            continue
