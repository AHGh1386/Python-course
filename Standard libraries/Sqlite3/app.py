import sqlite3

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * from Movies"
    cursor = conn.execute(command)
    # for item in cursor:
    #     print(item)
    movies = cursor.fetchall()
    print(movies)
