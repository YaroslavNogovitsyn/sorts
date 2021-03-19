a = []
a.append([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
a.append([-1, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1])
a.append([-1, 0, 0, 0, -1, 0, -1, 0, -1, 0, -1])
a.append([-1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1])
a.append([-1, 0, -1, 0, -1, -1, -1, -1, -1, 0, -1])
a.append([-1, 0, -1, 0, 0, 0, 0, 0, -1, 0, -1])
a.append([-1, 0, -1, -1, -1, -1, -1, -1, -1, 0, -1])
a.append([-1, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1])
a.append([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])


def printLab(a):
    for i in a:
        for j in i:
            if j == 0:
                print("    ", end='')
            elif j == -1:
                print('****', end='')
            else:
                if j < 10:
                    print(f" 0{j} ", end='')
                else:
                    print(f" {j} ", end='')
        print()
    print()


def findPath(a, x, y, number):
    a[x][y] = number
    if a[x + 1][y] == 0:
        findPath(a, x + 1, y, number + 1)
    if a[x][y + 1] == 0:
        findPath(a, x, y + 1, number + 1)
    if a[x][y - 1] == 0:
        findPath(a, x, y - 1, number + 1)
    if a[x - 1][y] == 0:
        findPath(a, x - 1, y, number + 1)


def getRoad(a, x, y):
    res = []

    res.append([x, y])
    if a[x + 1][y] == a[x][y] - 1:
        return res + getRoad(a, x + 1, y)
    if a[x - 1][y] == a[x][y] - 1:
        return res + getRoad(a, x - 1, y)
    if a[x][y + 1] == a[x][y] - 1:
        return res + getRoad(a, x, y + 1)
    if a[x][y - 1] == a[x][y] - 1:
        return res + getRoad(a, x, y - 1)

    return res


print("До обработки")
printLab(a)

findPath(a, 1, 1, 1)
print("После обработки")
printLab(a)

road = getRoad(a, 7, 9)
road.reverse()
print("Координаты пути:")
for i in road:
    print(i)
