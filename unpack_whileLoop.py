dict = {1: "Priya", 2: "chintu", 3: "Mary", 4: "Dasu"}
items = list(dict.items())

i = 0
while i < len(items):
    key, value = items[i]  
    print(key, value)
    i += 1
