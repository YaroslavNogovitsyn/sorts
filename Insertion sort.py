checklist = ['Кузнецов', 'Смирнов', 'Иванов', 'Павлов', 'Егоров', 'Краснов', 'Козлов', 'Орлов', 'Андреев', 'Макаров',
             'Зайцев', 'Соловьёв', 'Борисов', 'Федоров', 'Михайлов', 'Новиков', 'Морозов', 'Лебедев', 'Алексеев',
             'Гусев', 'Кисилёв', 'Ильин', 'Ковалев', 'Романов']
checklist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Обязательно начинаем с 1 в range()!
for i in range(1, len(checklist)):
    # Запоминаем "текущий" элемент
    value = checklist[i]
    # Формируем индекс для вставки
    j = i - 1
    # Пока индекс j больше 0 и элемент от индекса j меньше запомненного
    while checklist[j] > value and j >= 0:
        # Сдвигаем, освобождая место для запомненного в n элемента
        checklist[j + 1] = checklist[j]
        # Уменьшаем индекс j
        j = j - 1
    # Устанваливаем сохраненное значение в найденное место
    checklist[j + 1] = value
print(checklist)