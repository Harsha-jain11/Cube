# cube.py
import sys

def cube_of_number(num):
    return num ** 3

if len(sys.argv) != 2:
    print("Usage: python cube.py <number>")
    sys.exit(1)

num = int(sys.argv[1])
print("The cube of number is:", cube_of_number(num))
