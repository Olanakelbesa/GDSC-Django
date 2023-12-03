for i in range(100):
    if i < 10:
        print(f"0{i}", end=", ")
    elif i == 99:
        print(i, end="")
    else:
        print(i, end=", ")
