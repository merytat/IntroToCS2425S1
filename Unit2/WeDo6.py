#input
laps = []
laps.append(int(input("Enter lap 1:")))
laps.append(int(input("Enter lap 2:")))
laps.append(int(input("Enter lap 3:")))
laps.append(int(input("Enter lap 4:")))
laps.append(int(input("Enter lap 5:")))
# lap2 = int(input("Enter lap 2:"))
# lap3 = int(input("Enter lap 3:"))
# lap4 = int(input("Enter lap 4:"))
# lap5 = int(input("Enter lap 5:"))

print(laps)
laps.sort()
print(laps)
#use len to calculate number of elements and sustract 1
print("Your slowest lap was: ", laps[len(laps)-1])
#use -1 to access the last element
print("Your slowest lap was: ", laps[-1])
#use pop without an index to pop the last element
print("Your slowest lap was: ", laps.pop())




#process

#output