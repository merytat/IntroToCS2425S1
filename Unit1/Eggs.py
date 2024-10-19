#input
noEggs = int(input("Number of eggs: "))
price12 = float(input("Price per dozen"))
price1 = float(input("Price per egg"))

#processing
dozens = noEggs // 12
#print(dozens)
extraEggs = noEggs % 12 #extra eggs
#print(extraEggs)
total = dozens * price12 + extraEggs * price1
print("Total price: ", total)