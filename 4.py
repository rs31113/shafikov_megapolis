# Чтение данных из исходного файла
source_file = open("songs.txt", encoding="utf-8")
data = [elem.strip().split("?") for elem in source_file.readlines()][1:]
dictionary_date = dict()
dictionary_name = dict()
dictionary_song = dict()

# Обработка данных, сохранение в словари со всеми возможными ключами
for elem in data:
    streams, artist_name, song_name, date = elem
    if date not in dictionary_date:
        dictionary_date[date] = [[artist_name]]
    else:
        dictionary_date[date] += [[artist_name]]

    if artist_name not in dictionary_name:
        dictionary_name[artist_name] = [song_name]
    else:
        dictionary_name[artist_name] += [song_name]

    if f"{song_name}_{artist_name}" not in dictionary_song:
        dictionary_song[f"{song_name}_{artist_name}"] = [int(streams)]
    else:
        dictionary_song[f"{song_name}_{artist_name}"] += [int(streams)]

# Поиск артистов, чьи песни выпущены ранее 1990
valid_artists = set()
for date in dictionary_date.keys():
    year = int(date.split(".")[-1])
    if year < 1990:
        for name in dictionary_date[date]:
            valid_artists.add(*name)

print(*valid_artists)

# Создание и запись в конечный файл
result_file = open("songs_average.txt", "w", encoding="utf-8")
valid_artists_string = " ".join(valid_artists)
result_file.write(f"{valid_artists_string} \n")

# Нахождение среднего количества прослушиваний для песен до 1990
dictionary_streams = dict()
for name in valid_artists:
    for song in dictionary_name[name]:
        streams = dictionary_song[f"{song}_{name}"]
        average = sum(streams) // len(streams)
        dictionary_streams[average] = song
for elem in reversed(sorted(dictionary_streams)):
    result_file.write(f"{dictionary_streams[elem]}: {elem} \n")
    print(f"{dictionary_streams[elem]}: {elem}")
