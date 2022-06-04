#!/usr/bin/python3
if __name__ == "__main__":
    operator = {"+": add, "-": sub, "*": mul, "/": div}
    from calculator import add, sub, mul, div
    from sys import argv, exit

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit 1
    else:
        if argv[2] not in list(operator.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            exit 1
        else:
            a = int(argv[1])
            b = int(argv[2])
            print("{} {} {} = {}".format(a, argv[2], b, operator[argv[2]](a, b)))
