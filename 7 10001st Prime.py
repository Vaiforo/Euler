counter: int = 6
number: int = 14

while counter < 10001:
    for divider in range(2, int(number ** 0.5) + 10):
        if number % divider == 0:
            break
    else:
        print(number)
        counter += 1
    number += 1
print(number - 1)
