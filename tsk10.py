N = int(input("Введите число кубиков: "))

def count(left, last):
    if left == 0:
        return 1
    total = 0
    for new in range(1, min(left, last)):
        total += count(left - new, new)
    return total

print(count(N, N + 1) - 1)
