number = 600851475143
# number = 13195

for factor in range(int(number ** 0.5) + 1, 1, -1):
    if number % factor != 0:
        continue
    for mini_factor in range(2, int(factor ** 0.5) + 1):
        if factor % mini_factor == 0:
            break
    else:
        print(factor)
        break
