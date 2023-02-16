# подсчет количества букв в строке
s = input()
d = {}
for i in s:
    if i.isalpha():
        # if i in d:
        #     d[i] += 1
        # else:
        #     d[i] = 1
        #  тоже самое через метот get
        d[i] = d.get(i, 0) + 1
for i in sorted(d):  # функция sorted помогает сортировать в алфавитном порядке
    print(i, d[i])
