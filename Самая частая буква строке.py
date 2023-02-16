'''s = input()
ans = ''
anscnt = 0
for i in range(len(s)):
    nowcnt = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            nowcnt += 1
    if nowcnt > anscnt:
        ans = s[i]
        anscnt = nowcnt
print(ans)

Перебор посимвольно в строке
'''

'''s = input()
ans = ''
anscnt = 0
for now in range(len(s)):
    nowcnt = 0
    for j in range(len(s)):
        if now == s[j]:
            nowcnt += 1
    if nowcnt > anscnt:
        ans = now
        anscnt = nowcnt
print(ans)

Через множества преобразованное из строки
'''

s = input()
ans = ''
anscnt = 0
# создаём словарь и записываем новые символы из введёной строки
# оторые будут являться ключом
dct = {}
for now in s:
    if now not in dct:
        dct[now] = 0
    dct[now] += 1
# значение ключа из словаря dct
for key in dct:
    if dct[key] > anscnt:
        anscnt = dct[key]
        ans = key
print(ans)
