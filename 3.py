# Чтение данных из исходного файла
source_file = open("songs.txt", encoding="utf-8")
data = [elem.strip().split("?") for elem in source_file.readlines()][1:]
dictionary = dict()

# Обработка данных, сохранение в словарь с ключом - названием песни
for elem in data:
    streams, artist_name, song_name, date = elem
    if song_name not in dictionary:
        dictionary[song_name] = [[artist_name, streams, date]]
    else:
        dictionary[song_name] += [[artist_name, streams, date]]

# Принимаем запрос пользователя и гнаходим нужную песню в словаре
request = input()
try:
    print(f"Песня {request} принадлежит {dictionary[request][0]}")
except KeyError:
    print("К сожалению, песня не найдена.")
