brightness , threshold = map(str, input().split())

if float(brightness) >= float(threshold):
    print("ON")
else:
    print("OFF")
