# input full name of a person
fullName = input("Enter your full name: ")

# break the name inot first name,
#middle name and last name

firstSpace = fullName.find(" ")
middleLast = fullName[firstSpace+1:]
secondSpace = middleLast.find(" ")
middleName = middleLast[0:secondSpace+1]

#isolate first letter of first name
#make it capital
firstNameInitial = fullName[0:1].upper()

#isolate middle letter of middle nae
#find len() and //2
#make it capital
middleLetter = middleName[len(middleName) // 2: len(middleName) // 2 + 1].upper()

#isolate the last letter of the lastname
#find len() -1
# [-1]
# make it capital
lastLetter = fullName[len(fullName)-1:].upper()   # fullName[-1]

#output
print(firstNameInitial+middleLetter+lastLetter)