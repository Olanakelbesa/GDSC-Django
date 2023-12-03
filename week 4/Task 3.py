str = input("Please enter the word to check: ")
rev =str[::-1]

if str == rev:
    print(f"The word {str} is a palindrome.")
else:
    print(f"The word {str} is not a palindrome,")
    print(f"because {rev} is not equal to {str}.")