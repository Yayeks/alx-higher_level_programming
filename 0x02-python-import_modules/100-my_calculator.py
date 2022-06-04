#!/usr/bin/python3
if __name__ == "__main__":
    operator = {"+": add, "-": sub, "*": mul, "/": div}
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit 1

    if argv[2] not in list(operator.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit 1

    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, operator[argv[2]](a, b)))
