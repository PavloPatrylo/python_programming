print('hello')


from math import sqrt
print(sqrt(25))

import math as m
print(m.sqrt(25))

# command = input()
# match command:
#     case "start":
#         print("program has started without any erors")

numbers = []
for i in range(21):
    numbers.append(i)

count = 0 

for i in range(19): 
    if i % 2 != 0:
        count += 1
        if count % 3 == 0:
            continue  
        print(numbers[i+2])


# for i in numbers:
#     print(i)

# person = {'name': "John", 'age': 30}
# for i in person:
#     print(i, person[i])

