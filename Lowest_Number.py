N = int(input())
my_list = list(map(int, input().split()))

lowest = min(my_list)
index = my_list.index(lowest) + 1

print(f"{lowest} {index}")
