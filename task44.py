# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1 = first_element = int(input("Введите число для первого элемента "))
d = distribution = int(input("Введите разность эллементов"))
n = coll_element = int(input("Введите колличество элементов"))

an = a1 + (n - 1)*d
array = [i for i in range(a1,an + 1,d)]
print(array)
