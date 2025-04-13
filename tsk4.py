count = 0
while True:
    N = int(input())
    if N == 0:
        break
    if N % 2 == 0 and N >= 4:
        count += 1
print(count)
