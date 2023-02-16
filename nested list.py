a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]

# for i in a:
#     for j in i:
#         print(j, end=' ')
#     print()
print(a)

# обход по индексам по строчкам
for i in range(3):
    s = 0 #сумма обхода в строке
    for j in range(4):
        s += a[i][j]
        print(a[i][j], end=' ')
    print('= ', s)
print()

#обход по индексам по столбцам
for j in range(4):
    for i in range(3):
        print(a[i][j], end=' ')
    print()
print()

#вывод в обратном порядке, перевернутая таблица
for i in range(2, -1, -1):
    for j in range(3, -1, -1):
        print(a[i][j], end=' ')
    print()
