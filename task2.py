import math

number = float(input())
while number >= 2:
    number = math.sqrt(number)
    print(f"{number:.3f}", end=' ')
