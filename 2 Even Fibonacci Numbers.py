num1, num2 = 1, 2

even_fib_sum = 0
while num2 < 4000000:
    if num2 % 2 == 0:
        even_fib_sum += num2
    num1, num2 = num2, num1 + num2
print(even_fib_sum)
