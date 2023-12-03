name = input("Enter your full name: ")
print(len(name))
print(name.upper())
ans = False
Lower_Name = name.lower()
for str in Lower_Name.split():
    if str == "smith":
        ans = True

if ans == True:
    print("Found")
else:
    print("Not Found!")