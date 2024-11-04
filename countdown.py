import sys
if len(sys.argv) != 2:
    print("Usage: python countdown.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

for i in range(n, 0, -1):
    print(i)
