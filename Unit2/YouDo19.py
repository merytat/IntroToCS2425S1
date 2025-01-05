import random
randNumbers = []

randNumbers.append(random.randint(1,10))
randNumbers.append(random.randint(1,10))
randNumbers.append(random.randint(1,10))
randNumbers.append(random.randint(1,10))
randNumbers.append(random.randint(1,10))
randNumbers.append(random.randint(1,10))
randNumbers.append(random.randint(1,10))
randNumbers.append(random.randint(1,10))
randNumbers.append(random.randint(1,10))
randNumbers.append(random.randint(1,10))

print(randNumbers)

counter = 0
sum = 0
for num in randNumbers:
    sum = sum + num
    if num % 2 == 0:
        counter = counter + 1

print("Total even: ", counter)
