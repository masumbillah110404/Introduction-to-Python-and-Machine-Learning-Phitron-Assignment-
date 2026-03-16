keywords = ['ai', 'data', 'model', 'learn', 'train', 'neural']

msg = input()
msg = msg.split(" ")

keyword_counter = 0
for text in msg:
    if text in keywords:
        keyword_counter += 1

if keyword_counter >= 2:
    print("AI Detected")
else:
    print("Not AI Related")
