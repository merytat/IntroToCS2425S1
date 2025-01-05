numbers = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
size = len(numbers)
print(numbers)

# add zeros
# numbers2 = []
# counter = 0
# for i in numbers:
#     if i == 0:
#         counter = counter + 1
#     else:
#         numbers2.append(i)
#
# for i in range(counter):
#     numbers2.append(0)

print(numbers)
numbers.append("a")
i = 0
while numbers[i] != "a":
    if numbers[i] == 0:
        numbers.append(0)
        numbers.pop(i)
    else:
        i = i + 1

numbers.remove("a")
print(numbers)


# print for visualization
#print(numbers2)

# remove zeros
# for i in range(0,size):
#     if numbers[i] == 0:


