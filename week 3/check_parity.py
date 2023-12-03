def parity():
    number = int(input("Enter number: "))
    while number != 0:
        if number % 2 == 0:
            print(f"{number} is Even number")
        elif number % 2 == 1:
            print(f"{number} is Odd number")
        number = int(input("Enter number: "))
parity()