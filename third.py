import csv

file = open('data.csv', 'r')
rdr = csv.reader(file, delimiter=',')
summ = 0
print('Нужно купить:')
for row in rdr:
    print(f'{row[0]} - {row[1]} шт. за {row[2]} руб.')
    summ += int(row[1]) * int(row[2])
print(f'Итоговая сумма: {summ} руб.')
file.close()
