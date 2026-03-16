N = int(input())
my_list = list(map(int, input().split()))

evens = []
odds = []
positive = []
negative = []

for x in my_list:
    if x % 2 == 0:
        evens.append(x)
    else:
        odds.append(x)
    
    if x > 0:
        positive.append(x)
    elif x < 0:
        negative.append(x)

print(f"Even: {len(evens)}")
print(f"Odd: {len(odds)}")
print(f"Positive: {len(positive)}")
print(f"Negative: {len(negative)}")
