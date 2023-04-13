# Урок 1. Ввод-Вывод, операторы ветвления
# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение
def zadacha1():
    number = int(input("Введите номер дня недели: "))
    if number <= 0 or number >= 8:
        print("нет такого дня недели")
    elif number == 1:
        print("Понедельник")
    elif number == 2:
        print("Вторник")
    elif number == 3:
        print("Среда")
    elif number == 4:
        print("Четверг")
    elif number == 5:
        print("Пятница")
    elif number == 6:
        print("Суббота")
    elif number == 7:
        print("Воскресенье")


# zadacha1()

# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21


def zadacha2():
    x1 = input("Введите координату x для первой точки: ")
    y1 = input("Введите координату y для первой точки: ")
    x2 = input("Введите координату x для второй точки: ")
    y2 = input("Введите координату y для второй точки: ")
    razn_x = int(x2) - int(x1)
    razn_y = int(y2) - int(y1)
    distance = ((razn_x**2) + (razn_y**2)) ** 0.5
    print("Расстояние между точками: {:.2f}".format(distance))


# zadacha2()

# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
# точек в этой четверти (x и y).
# 1 -> x > 0, y > 0


# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8
