brightness = list(map(int, input().split()))

avg_brightness = sum(brightness) / len(brightness)

if avg_brightness < 85:
    print("Dark Image")
elif 85 <= avg_brightness <= 170:
    print("Normal Image")
else: 
    print("Bright Image")