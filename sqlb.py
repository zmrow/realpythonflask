import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    cities = [
            ('Boston', 'MA', 600000),
            ('Chicago', 'IL', 270000),
            ('Houston', 'TX', 210000),
            ('Phoenix', 'AZ', 150000)
            ]

    c.executemany('INSERT INTO population VALUES(?,?,?)', cities)
