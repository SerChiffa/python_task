
gender = {
    'male': 'Дорогой',
    'famale': 'Дорогая'
}

user = [
    ['Семён', 'Семёнович', 32.56, 'male'],
    ['Инга', 'Викторовна', 235.13, 'famale'],
    ['Владислав', 'Степанович', 145.07, 'male'],
]

# name = 'Семён'
# mid_name = 'Семёнович'
# balance = 23.56

for name, midname, balance, g in user:
    text = f'{gender[g]} {name} {midname}, баланс вашего счёта составляет {balance}.'
    print(text)
