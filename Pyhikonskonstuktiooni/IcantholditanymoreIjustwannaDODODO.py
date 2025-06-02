# import tkinter as tk
# from tkinter import Button, Entry, Label, Toplevel, messagebox
# from tkinter import ttk
# import sqlite3
# from venv import create
# global entries
# import subprocess

# create_table0 = '''
# CREATE TABLE IF NOT EXISTS movies (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   title TEXT NOT NULL,
#   director_id INTEGER,
#   release_year INTEGER,
#   genre_id INTEGER,
#   duration INTEGER,
#   rating REAL,
#   language_id INTEGER,
#   country_id INTEGER,
#   description TEXT,
#   FOREIGN KEY (director_id) REFERENCES director(id),
#   FOREIGN KEY (genre_id) REFERENCES genres(id),
#   FOREIGN KEY (language_id) REFERENCES languages(id),
#   FOREIGN KEY (country_id) REFERENCES countries(id)
# );
# '''

# insert_into = '''
# INSERT INTO movies (title, directors, release_year, genre, duration, rating, language, country, description) VALUES
# ('The From In With.', 'Francis Ford Coppola', 1994, 'Drama', 142, 9.3, 'English', 'USA', 'The In With By On. A In From By The At. On A With By By On To A.'),
# ('The By On To.', 'Christopher Nolan', 2010, 'Sci-Fi', 148, 8.8, 'English', 'UK', 'The A The On The In. By To A At On The. From The In With At In To A.'),
# ('In The With On.', 'Quentin Tarantino', 1972, 'Crime', 175, 9.2, 'English', 'USA', 'On From The By At The A. In From By With To On. A The By In With At On To A.'),
# ('The A To From.', 'Steven Spielberg', 1994, 'Adventure', 154, 8.9, 'English', 'France', 'With By In The A On. The With To A At The From. On A From With At By The.'),
# ('On The From With.', 'Martin Scorsese', 2008, 'Action', 152, 9.0, 'English', 'Germany', 'The A By On In The. At With To A From On The. With On By The A In To From.'),
# ('From The By With.', 'Christopher Nolan', 1960, 'Drama', 134, 8.5, 'English', 'UK', 'The A On From The At. With To By In A The On. At The In From With By To A.'),
# ('The By On A.', 'Francis Ford Coppola', 1999, 'Thriller', 112, 7.8, 'English', 'USA', 'A The On By In The At. From With A On By To The. In The By With At A From.'),
# ('On A The From.', 'Quentin Tarantino', 2015, 'Comedy', 126, 7.9, 'English', 'Italy', 'By With A On In The From. The By At A With On To. At In The By From With A.'),
# ('By The On From.', 'Steven Spielberg', 1975, 'Action', 143, 8.7, 'English', 'France', 'A With On The By From In. The A At On With To From. By In The A From With At On.'),
# ('From With The By.', 'Martin Scorsese', 1980, 'Crime', 163, 9.1, 'English', 'Germany', 'On The A By In The From. With By On A The In From. To The In At By With On A.');
# '''

# # Keeled
# create_table_keeled = '''
# CREATE TABLE IF NOT EXISTS languages (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL
# );
# '''

# create_table_riigid = '''
# CREATE TABLE IF NOT EXISTS countries (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL
# );
# '''

# create_table_žanrid = '''
# CREATE TABLE IF NOT EXISTS genres (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL
# );
# '''

# create_table_režissöörid = '''
# CREATE TABLE IF NOT EXISTS directors (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL
# );
# '''

# def create_table():
#     try:
#         conn = sqlite3.connect('moviesWORD.db')
#         cursor = conn.cursor()
#         print("Ühendus loodud")
#         # Siia päringud
#         cursor.execute(create_table0)
#         cursor.execute(create_table_keeled)
#         cursor.execute(create_table_riigid)
#         cursor.execute(create_table_žanrid)
#         cursor.execute(create_table_režissöörid)

#         print("Tabel loodud")

#     except sqlite3.Error as error:
#         print("Tekkis viga andmebaasiga ühendamisel:", error)
#     finally:
#         if conn:
#             conn.close()

# def insert():
#     try:
#         conn = sqlite3.connect('moviesWORD.db')
#         cursor = conn.cursor()
#         cursor.execute(insert_into)
#         print("Tebel täidetud")

#     except sqlite3.Error as error:
#         print("Tekkis viga andmebaasiga ühendamisel:", error)
#     finally:
#         if conn:
#             conn.close()


# def täida_tabel():
#     try:
#         conn = sqlite3.connect('moviesWORD.db')
#         cursor = conn.cursor()
#         print("Ühendus loodud")

#         # Teostame päringu, et lugeda kõik andmed tabelist 'movies'
#         cursor.execute("SELECT * FROM movies")
#         rows = cursor.fetchall() # shows result in the screen

#         # Väljastame kõik loetud read
#         for row in rows:
#             print(row)

#     except sqlite3.Error as error:
#         print("Tekkis viga andmebaasiga ühendamisel või päringu teostamisel:", error)
#     finally:
#         if conn:
#             conn.close()
#             print("Ühendus suleti")

# create_table()
# insert()
# täida_tabel()

import sqlite3

# --- Table Creation SQL ---
create_table_movies = '''
CREATE TABLE IF NOT EXISTS movies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  director_id INTEGER,
  release_year INTEGER,
  genre_id INTEGER,
  duration INTEGER,
  rating REAL,
  language_id INTEGER,
  country_id INTEGER,
  description TEXT,
  FOREIGN KEY (director_id) REFERENCES directors(id),
  FOREIGN KEY (genre_id) REFERENCES genres(id),
  FOREIGN KEY (language_id) REFERENCES languages(id),
  FOREIGN KEY (country_id) REFERENCES countries(id)
);
'''

create_table_directors = '''
CREATE TABLE IF NOT EXISTS directors (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);
'''

create_table_genres = '''
CREATE TABLE IF NOT EXISTS genres (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);
'''

create_table_languages = '''
CREATE TABLE IF NOT EXISTS languages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);
'''

create_table_countries = '''
CREATE TABLE IF NOT EXISTS countries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);
'''

# --- Static Data Insertion ---
def insert_static_data(cursor):
    data = {
        "directors": ["Francis Ford Coppola", "Christopher Nolan", "Quentin Tarantino", "Steven Spielberg", "Martin Scorsese"],
        "genres": ["Drama", "Sci-Fi", "Crime", "Adventure", "Action", "Thriller", "Comedy"],
        "languages": ["English"],
        "countries": ["USA", "UK", "France", "Germany", "Italy"]
    }
    for table, values in data.items():
        for val in values:
            cursor.execute(f"INSERT OR IGNORE INTO {table} (name) VALUES (?)", (val,))

# --- Helper to Fetch ID ---
def get_id(cursor, table, name):
    cursor.execute(f"SELECT id FROM {table} WHERE name = ?", (name,))
    result = cursor.fetchone()
    return result[0] if result else None

# --- Create Tables ---
def create_tables():
    conn = sqlite3.connect('moviesWORD.db')
    cursor = conn.cursor()
    cursor.execute(create_table_directors)
    cursor.execute(create_table_genres)
    cursor.execute(create_table_languages)
    cursor.execute(create_table_countries)
    cursor.execute(create_table_movies)
    conn.commit()
    conn.close()
    print("Tabelid loodud")

# --- Insert Movie Records ---
def insert_movies():
    conn = sqlite3.connect('moviesWORD.db')
    cursor = conn.cursor()

    insert_static_data(cursor)  # Fill lookup tables first

    movies = [
        ("The From In With.", "Francis Ford Coppola", 1994, "Drama", 142, 9.3, "English", "USA", "The In With By On. A In From By The At."),
        ("The By On To.", "Christopher Nolan", 2010, "Sci-Fi", 148, 8.8, "English", "UK", "The A The On The In. By To A At On The."),
        ("In The With On.", "Quentin Tarantino", 1972, "Crime", 175, 9.2, "English", "USA", "On From The By At The A. In From By With To On."),
        ("The A To From.", "Steven Spielberg", 1994, "Adventure", 154, 8.9, "English", "France", "With By In The A On. The With To A At The From."),
        ("On The From With.", "Martin Scorsese", 2008, "Action", 152, 9.0, "English", "Germany", "The A By On In The. At With To A From On The."),
        ("From The By With.", "Christopher Nolan", 1960, "Drama", 134, 8.5, "English", "UK", "The A On From The At. With To By In A The On."),
        ("The By On A.", "Francis Ford Coppola", 1999, "Thriller", 112, 7.8, "English", "USA", "A The On By In The At. From With A On By To The."),
        ("On A The From.", "Quentin Tarantino", 2015, "Comedy", 126, 7.9, "English", "Italy", "By With A On In The From. The By At A With On To."),
        ("By The On From.", "Steven Spielberg", 1975, "Action", 143, 8.7, "English", "France", "A With On The By From In. The A At On With To From."),
        ("From With The By.", "Martin Scorsese", 1980, "Crime", 163, 9.1, "English", "Germany", "On The A By In The From. With By On A The In From.")
    ]

    for movie in movies:
        title, director, year, genre, duration, rating, language, country, desc = movie
        director_id = get_id(cursor, "directors", director)
        genre_id = get_id(cursor, "genres", genre)
        language_id = get_id(cursor, "languages", language)
        country_id = get_id(cursor, "countries", country)

        cursor.execute('''
            INSERT INTO movies (title, director_id, release_year, genre_id, duration, rating, language_id, country_id, description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, director_id, year, genre_id, duration, rating, language_id, country_id, desc))

    conn.commit()
    conn.close()
    print("Filmid lisatud")

# --- Display Movies ---
def täida_tabel():
    conn = sqlite3.connect('moviesWORD.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT m.id, m.title, d.name, m.release_year, g.name, m.duration, m.rating,
           l.name, c.name, m.description
    FROM movies m
    JOIN directors d ON m.director_id = d.id
    JOIN genres g ON m.genre_id = g.id
    JOIN languages l ON m.language_id = l.id
    JOIN countries c ON m.country_id = c.id
    ''')

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

# --- Run the Whole Flow ---
create_tables()
insert_movies()
täida_tabel()

