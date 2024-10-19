# input the word
word = input("Word: ")

# find the middle letter
    # //2 - divide by 2 - integer divisio
num = len(word) // 2

# slice the string to take the letter
# before the middle, the letter in the
# middle, and the letter after the middle
middleLetters = word[num -1: num + 2]

# output the 3 letters
print("Middle Letters: ", middleLetters)
