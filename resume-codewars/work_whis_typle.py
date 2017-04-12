"""
Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        command = input().split()
        if command[0] == 'insert':
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(lst)
        elif command[0] == 'remove':
            lst.remove(command[1])
        elif command[0] == 'append':
            lst.append(int(command[1]))
        elif command[0] == 'sort':
            lst = sorted(lst)
        elif command[0] == 'pop':
            lst.pop()
        elif command[0] == 'reverse':
            lst = reversed(lst)