predictions = list(map(str, input().split()))

count_A = 0
count_B = 0

margin = len(predictions) * 0.7

for x in predictions:
    if x == 'A':
        count_A += 1
    else:
        count_B += 1

if float(count_A) >= margin or float(count_B) >= margin:
    print("Biased Model")
else:
    print("Fair Model")