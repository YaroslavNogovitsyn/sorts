def qsort(a):
    if len(a) == 2:
        if a[0] > a[1]:
            a[0], a[1] = a[1], a[0]
        return a
    elif len(a) > 2:
        average = a[len(a) // 2]
        sp1 = []  # Элементы меньше среднего
        sp2 = []  # Элементы, равные среднему
        sp3 = []  # Элементы болше среднего
        for i in a:
            if i < average:
                sp1.append(i)
            elif i > average:
                sp3.append(i)
            else:
                sp2.append(i)
        return qsort(sp1) + sp2 + qsort(sp3)
    else:
        return a


a = [5, 8, 1, 5, 3, 5, 2, 0, 2, 5, 2]
print(a)
a = qsort(a)
print(a)
