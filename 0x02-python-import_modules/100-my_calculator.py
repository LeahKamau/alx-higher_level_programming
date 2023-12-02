#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    ac = len(argv)

    if ac != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])

    if argv[2] == "+":
        print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
        exit(0)
    elif argv[2] == "-":
        print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
        exit(0)
    elif argv[2] == "*":
        print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
        exit(0)
    elif argv[2] == "/":
        print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
