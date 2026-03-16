T = int(input())
my_list = []

for _ in range(T):
    inp = int(input())
    my_list.append(inp)

for x in my_list:
    x = str(x)[::-1]
    for i in x:
        print(i, end =" ")
    print()