import sqlite3 as sq
try:
    with sq.connect("test2.db") as con:
        cur = con.cursor()

        lstcar = [
            ("AUDI", 20000),
            ("FORD", 1000),
            ("BMW", 15000)
        ]

        cur.execute("""CREATE TABLE IF NOT EXISTS car(
            car_id INTEGER PRIMARY KEY,
            car_name TEXT,
            cost INTEGER)
            """)

        cur.execute("INSERT INTO car VALUES (NULL, ?, ?)", )
except Exception as ex:
    print(ex)
finally:
    if con:
        con.close()