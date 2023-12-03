ch = input("Please enter the patter to be printed: ").lower()
if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    print("Vowels are not allowed in the input")
elif len(ch) > 1:
    print("The length of the character should be 1")
else:
    for i in range(10):
        if i % 2 == 1:
           print(ch*i)