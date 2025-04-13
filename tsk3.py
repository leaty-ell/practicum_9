N = int(input())
max_packs = 0
best_group = 0

for group in range(2, N + 1):
    if N % group == 0:
        packs_per_person = N // group
        if packs_per_person > max_packs:
            max_packs = packs_per_person
            best_group = group

print(best_group)
