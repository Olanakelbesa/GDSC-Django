string = input("Enter string: ")
word_length = [len(str) for str in string.split()]
print(word_length)
for l in word_length:
    if l > 10:
        print("Long")
    else:
        print("Short")