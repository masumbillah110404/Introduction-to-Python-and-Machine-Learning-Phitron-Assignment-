N = int(input())
target = float(input())

losses = []
for _ in range(N):
    x = float(input())
    losses.append(x)

avg_loss = sum(losses) / len(losses)

if avg_loss <= target:
    print("PASS")
else:
    print("RETRY")
