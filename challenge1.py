def plus(a, b):
    return a+b


def minus(a, b):
    return a-b


def multply(a, b):
    return a*b


def devide(a, b):
    return a/b


calculating = True


while calculating:
    a = int(input("Choose a number:"))
    b = int(input("Choose another one:"))
    operation = input(
        "Choose an operation: \n\tOptions are: +, -, * or /. \n\tWrite 'exit' to finish")1

    if operation == "+":
        print("Result:", plus(a, b))

    elif operation == "-":
        print("Result:", minus(a, b))

    elif operation == "-":
        print("Result:", multply(a, b))

    elif operation == "-":
        print("Result:", devide(a, b))

    elif operation == "exit":
        calculating = False
