x, y, z = map(int, input().split())

my_list = []

my_list.append(x)
my_list.append(y)
my_list.append(z)

my_list.sort()

print(f"{my_list[0]} {my_list[-1]}")
