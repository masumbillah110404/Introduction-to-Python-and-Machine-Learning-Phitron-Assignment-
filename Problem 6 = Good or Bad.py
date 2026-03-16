N = int(input())
my_list = []

for _ in range(N):
    x = input()
    my_list.append(x)

sub_str_1 = '010'
sub_str_2 = '101'

for x in my_list:
    if sub_str_1 in x or sub_str_2 in x:
        print("Good")
    else:
        print("Bad")