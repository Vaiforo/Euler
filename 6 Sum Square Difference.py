number: int = 100

sum_of_squares: int = sum(map(lambda x: x ** 2, range(1, number + 1)))
square_of_sum: int = sum(range(1, number + 1)) ** 2

print(f"{sum_of_squares} - {square_of_sum} = {sum_of_squares - square_of_sum}")
