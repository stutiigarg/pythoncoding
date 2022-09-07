def add(x, y):
    print(x, "+", y, '=', x + y)


def sub(x, y):
    print(x, "-", y, '=', x - y)


def div(x, y):
    print(x, "/", y, '=', x / y)


def mul(x, y):
    print(x, "*", y, '=', x * y)


print("enter your choice: ")
print("1 for add")
print("2 for subtract")
print("3 for divide")
print("4 for multiply")

i = input("enter the choice = ")

if i in ("1", "2", "3", "4"):
    x = int(input("enter first no = "))
    y = int(input("enter second no = "))

    if i == "1":
        print(add(x, y))
    elif i == "2":
        print(sub(x, y))
    elif i == "3":
        print(div(x, y))
    else:
        print(mul(x, y))


