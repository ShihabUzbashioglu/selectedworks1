import sqlite3 as sql
con=sql.connect("database.db")
cur=con.cursor()
query="""CREATE TABLE IF NOT EXISTS students(
name VARCHAR(20),
class VARCHAR(5),
section VARCHAR(5),
percent int
)
"""
cur.execute(query)