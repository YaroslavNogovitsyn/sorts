year_of_books = list(map(int, input("Введите годы книг:").split()))
for i in range(len(year_of_books)):
    min_index = i
    min_value = year_of_books[i]
    for j in range(i + 1, len(year_of_books)):
        if year_of_books[j] < min_value:
            min_index = j
            min_value = year_of_books[j]
    year_of_books[min_index] = year_of_books[i]
    year_of_books[i] = min_value
print(year_of_books)
# 1955 1644 1849 1784 2005 1994


# year_of_books = [int(i) for i in input().split()]
year_of_books = list(map(int, input("Введите годы книг:").split()))
for i in range(len(year_of_books) - 1):
    min_index = i
    for j in range(i + 1, len(year_of_books)):
        if year_of_books[j] < year_of_books[min_index]:
            min_index = j
    year_of_books[i], year_of_books[min_index] = year_of_books[min_index], year_of_books[i]
print(year_of_books)
