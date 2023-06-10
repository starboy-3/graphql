# GraphQL Python Mafia game

### Запуск сервера
```
docker build . -t starboy369/graphql-mafia
docker run -p 8080:8080 starboy369/graphql-mafia
```

### Запуск клиента

```
python3 -m pip install -r requirements.txt
python3 client.py "<YOUR_NAME>"
```

### Команды

```
'all games' - вывести все игры
'games finished' - вывести все законченные игры
'games unfinished' - вывести все незаконченные игры
'game <id>' - получить всю информацию об игре
'game <id> score' - получить счет игры
'add comment <id> <comment>' - добавить комментарий к игре
'exit' or Ctrl^C - выйти из программы
```