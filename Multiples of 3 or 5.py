border = 1000

answer = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, border)))
print(sum(answer))
# print(answer)
