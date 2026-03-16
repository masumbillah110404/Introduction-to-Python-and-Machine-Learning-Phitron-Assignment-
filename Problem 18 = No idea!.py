n , m = map(int, input().split())

array = list(map(int, input().split()))

set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

happiness = 0

for x in array:
    if x in set_A:
        happiness += 1
    elif x in set_B:
        happiness -= 1
    else:
        continue

print(happiness)