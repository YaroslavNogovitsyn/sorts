def printData(lst):
    # p - Маркер номера позиуии, в которой в списке находится "не ноль"
    # Задаем индекс последнего элемента
    p = len(lst) - 1

    # Пока первый встречный с конца элемент равен 0, уменьшаем p
    while lst[p] == 0 and p >= 0:
        p -= 1
    if p == 0:
        print(0)
    else:
        for i in range(p, -1, -1):
            print(alphabet[lst[i]], end="")
        print()


# Функция сложения длинных чисел
def summLong(a, b, base):
    # Создаем копию списка "а" в переменную acopy для того, чтобы не изменить оригинал
    acopy = a.copy()
    c = []
    for i in range(len(acopy) - 1):
        summa = acopy[i] + b[i]
        if summa >= base:
            acopy[i + 1] += 1
            summa -= base
        c.append(summa)
    return c

alphabet = "0123456789"
alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet += "abcdefghijklmnopqrstuvwxyz"
alphabet += "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet += "абвгдежзийклмнопрстуфхцчшщъыьэюя"
a = [10, 13, 14, 11, 0, 0]
b = [10, 11, 10, 11, 0, 0]
printData(a)
printData(b)
c = summLong(a, b, 16)
printData(c)
