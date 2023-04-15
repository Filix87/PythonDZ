# Урок 2. Циклы (for, while)

# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def task1():
    def f_list(n):
        f = [1] * n
        for i in range(1, n):
            f[i] = f[i - 1] * (i + 1)
        return f

    n = int(input("Введите число: "))
    print(f_list(n))


# task1()

# -----------------
# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.


def task2():
    print(f"X\tY\tZ\t¬(X ∧ Y) ∨ Z")
    for x in [True, False]:
        for y in [True, False]:
            for z in [True, False]:
                result = not (x and y) or z
                print(f"{x}\t{y}\t{z}\t{result}")


# task2()
# -----------------
# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2


def task3():
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    print
    print(f' "{str1}", "{str2}" ')
    counts = {}
    for char in str1:
        count = str2.count(char)
        counts[char] = count
    for char, count in counts.items():
        print(char, "-", count, end="   ")


# task3()

# -----------------
# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]


def task4():
    n = int(input("Введите число: "))
    str = list(range(-n, n + 1))
    str = str[-2:] + str[:-2]
    print(f"{n} -> {str}")


task4()
