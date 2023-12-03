sum = 0
count_three = 0
count_five = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum += i
        if i % 3 == 0:
            count_three += 1
            print("Three")
        elif i % 5 == 0:
            count_five += 1
            print("Five")
print(f"Total: {sum}")
print(f"Three: {count_three}")
print(f"Five: {count_five}")