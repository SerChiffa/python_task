a = [0, 5, 2, 1, 1, 0, 4, 0, 4, 5, 2, 1, 4, 0, 3, 2, 3]
count = [0] * 6
for i in a:
    count[i] += 1
print(count)
for i in range(6):
    if count[i] > 0:
        print(i, count[i])
        # print((str(i) + ' ') * count[i], end='')
        # выведет в строчку через пробел по возрастанию
