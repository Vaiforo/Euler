number: int = 20
dividers: list[int] = [2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
while True:
    number += 1
    for divider in dividers:
        if number % divider != 0:
            break
    else:
        print(number)
