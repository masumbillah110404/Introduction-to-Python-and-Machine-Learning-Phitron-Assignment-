N = int(input())
my_list = list(map(int, input().split()))

maximum = max(my_list)
minimum = min(my_list)

max_index = my_list.index(maximum)
min_index = my_list.index(minimum)

my_list[max_index] = minimum
my_list[min_index] = maximum

for i in my_list:
    print(i, end=" ")