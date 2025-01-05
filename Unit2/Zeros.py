list = [23,0,0,45,0,1,0,0,0,45,23,1,0,3,78]

list2 = []
counter = 0
for i in list:
    if i != 0:
        list2.append(i)
    else:
        counter = counter + 1

for _ in range(counter):
    list2.append(0)

for i in list:
    if i == 0:
        list.remove(i)
        list.append(i)


