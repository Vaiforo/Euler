max_palindrome: int = 0
for number_one in range(999, 99, -1):
    for number_two in range(999, number_one - 1, -1):
        product: int = number_one * number_two
        if str(product) == str(product)[::-1] and product > max_palindrome:
            print(product, number_one, number_two)
            max_palindrome = product
