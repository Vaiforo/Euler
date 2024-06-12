flag = True
for number_one in range(999, 100, -1):
    for number_two in range(999, number_one + 1, -1):
        product = number_one * number_two
        if str(product)[:3] == str(product)[3::][::-1]:
            print(product)
            flag = False
            break
    if not flag:
        break
