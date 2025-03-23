"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
def main():
    info=[
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Варя', 'age': 33, 'job': 'Teacher'}
    ]
    with open('date.csv', 'w', encoding='utf-8') as f:
        fields=['name', 'age', 'job']
        writer=csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in info:
            writer.writerow(user)


if __name__ == "__main__":
    main()
