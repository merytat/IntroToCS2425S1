
counter = 0
#repeated
number = int(input("Enter a number of 0 to exit: "))
while number != 0:
    if (number % 3 == 0 or number % 5 == 0) and (number % 3 != 0 or number % 5 != 0):
        print(number, "is a magic number")
        counter = counter + 1
    else:
        print(number, "is not a magic number")
    print("magic numbers: ", counter)
    number = int(input("Enter a number of 0 to exit: "))

print("Good bye!")
