# sort and 4 lists
times = []
runner1 = []
runner2 = []
runner3 = []

runner1.append(input("Enter runner 1 name: "))
runner1.append(int(input("Enter the time for " + runner1[0])))
times.append(runner1[1])

runner2.append(input("Enter runner 2 name: "))
runner2.append(int(input("Enter the time for " + runner2[0])))
times.append(runner2[1])

runner3.append(input("Enter runner 3 name: "))
runner3.append(int(input("Enter the time for " + runner3[0])))
times.append(runner3[1])

times.sort()

if(runner1[1] == times[0]):
    if(runner1[1] == runner2[1] or runner1[1] == runner3[1]):
        print("There was a tie")
    print("Fastest runner was: ", runner1[0])
elif(runner2[1] == times[0]):
    print("Fastest runner was: ", runner2[0])
else:
    print("Fastest runner was: ", runner3[0])


# Alternatives
# min() - calculates the minimum value on a list
# parallel lists - 