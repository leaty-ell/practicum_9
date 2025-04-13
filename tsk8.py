x = int(input())
count = 0
for a in range(1, int(x**0.5) + 1):
    b_squared = x - a**2
    if b_squared <= 0:
        continue
    b = int(b_squared**0.5)
    if b * b == b_squared and a <= b:
        count += 1
print(count)
