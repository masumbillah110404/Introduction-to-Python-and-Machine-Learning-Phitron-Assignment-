string = input()

dictionary = {}

for letter in string:
    if letter in dictionary.keys():
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1

dictionary = dict(sorted(dictionary.items()))


for key,val in dictionary.items():
    print(f"{key} : {val}")