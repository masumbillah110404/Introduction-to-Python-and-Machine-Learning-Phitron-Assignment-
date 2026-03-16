msg = input()
msg = msg.split(" ")

happy_mood = ['happy', 'joy', 'smile']
sad_mood = ['sad', 'cry', 'angry']

neutral = True
for text in msg:
    if text in happy_mood:
        print("Happy Mood")
        neutral = False
        break
    elif text in sad_mood:
        print("Sad Mood")
        neutral = False
        break

if neutral:
    print("Neutral Mood")