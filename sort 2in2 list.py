"""# Функция, возвращающая одномерный список индексов двумерного списка
def getIndexArray(myList):
    ret = []
    for i in range(len(myList)):
        for j in range(len(myList)):
            # Добавляем ячейку
            ret.append([])
            ret[i * len(myList) + j].append(i)
            ret[i * len(myList) + j].append(j)
    return ret


# Возвращает отсортированный двумерный список
def getSortedArray(myList, idx):
    for i in range(len(idx) - 1):
        for j in range(len(idx) - 1 - i):
            # По индексам из idx сравниваем два соседних элемента
            if myList[idx[j][0]][idx[j][1]] > myList[idx[j + 1][0]][idx[j + 1][1]]:
                myList[idx[j][0]][idx[j][1]], myList[idx[j + 1][0]][idx[j + 1][1]] = \
                    myList[idx[j + 1][0]][idx[j + 1][1]], myList[idx[j][0]][idx[j][1]]
    return myList


a = [[16, 6, 11, 7],
     [5, 12, 13, 14],
     [3, 9, 15, 10],
     [1, 4, 8, 2]]

idx = getIndexArray(a)
print(f"Исходный список:\n{a}\n\nОтсортированный:\n{getSortedArray(a, idx)}")"""
a = [[16, 6, 11, 7],
     [5, 12, 13, 14],
     [3, 9, 15, 10],
     [1, 4, 8, 2]]


# Возвращает отсортированный двумерный список
def getSortedArray(myList):
    """arr1 = []  # создадим пустой массив
    for row in a:  # пройдёмся по всем элементам входного массива
        for elem in row:
            arr1.append(elem)"""
    arr1 = sorted([elem for row in a for elem in row])

    # lst = sorted(arr1)

    ret = []
    for i in range(len(arr1) // 4):
        ret.append([])
        for j in range(len(arr1) // 4):
            ret[i].append(arr1[4 * i] + j)

    return ret


print(getSortedArray(a))
