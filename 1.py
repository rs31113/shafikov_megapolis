# Чтение данных из исходного файла
source_file = open("songs.txt", encoding="utf-8")
data = [elem.strip().split("?") for elem in source_file.readlines()][1:]
dictionary = dict()

 # Обработка данных, сохранение в словарь с ключом - именем артиста
for elem in data:
    streams, name, song_name, date = elem
    if name not in dictionary:
        dictionary[name] = [[song_name, streams, date]]
    else:
        dictionary[name] += [[song_name, streams, date]]

# Запись данных в конечный файл "songs_artst.csv"
request = input()
result_file = open("songs_artst.csv", "w", encoding="utf-8")
result_file.write("track_name,streams,date\n")
if request in dictionary:
    for song in dictionary[request]:
        song = ",".join(song) + "\n"
        result_file.write(song)
else:
    print("No such artist.")
