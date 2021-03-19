number_of_players = list(map(int, input("Введите число участников в каждой команде через пробел:").split()))
for i in range(len(number_of_players) - 1):
    for j in range(len(number_of_players) - 1 - i):
        if number_of_players[j] > number_of_players[j + 1]:
            number_of_players[j], number_of_players[j + 1] = number_of_players[j + 1], number_of_players[j]
print(number_of_players)

