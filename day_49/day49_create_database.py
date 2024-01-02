

import sqlite3



def create_database():
    connection = sqlite3.connect("movies.db")
    print(connection.total_changes)

    cursor = connection.cursor()
    print("create database")

    print(connection.total_changes)
    #create table
    cursor.execute("CREATE table MOVIES (year TEXT, title TEXT, genre Text)")

def insert_rows():
    connection = sqlite3.connect("movies.db")
    print(connection.total_changes)

    cursor = connection.cursor()
    cursor.execute("INSERT INTO MOVIES VALUES ('2009', 'Brothers', 'Drama')")
    cursor.execute("INSERT INTO MOVIES VALUES ('2002', 'Spider man', 'Sci-fi')")
    cursor.execute("INSERT INTO MOVIES VALUES ('2009', 'WatchMen', 'Drama')")
    cursor.execute("INSERT INTO MOVIES VALUES ('2010', 'Inception', 'Sci-fi')")
    cursor.execute("INSERT INTO MOVIES VALUES ('2009', 'Avatar', 'Fantasy')")
    connection.commit()
    connection.close()

def reading_all_movies():
    connection = sqlite3.connect("movies.db")
    print(connection.total_changes)
    cursor = connection.cursor()

    connection.sqllite3.connect
    rows = cursor.execute("SELECT * FROM MOVIES").fetchall()
    print(rows)

def reading_movie(title):
    connection = sqlite3.connect("movies.db")
    print(connection.total_changes)

    cursor = connection.cursor()
    rows = cursor.execute("SELECT * FROM MOVIES where title = ?", (title,),).fetchall()
    print(rows)

def get_movies_by_year(year):
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    rows = cursor.execute("SELECT * FROM MOVIES where year = ?", (year,),).fetchall()
    print(rows)

def delete_movies():
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM MOVIES;')
    connection.commit()
    connection.close()