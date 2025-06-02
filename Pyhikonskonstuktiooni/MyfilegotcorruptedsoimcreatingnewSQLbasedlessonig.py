# import tkinter as tk
# from tkinter import Button, Entry, Label, Toplevel, messagebox
# from tkinter import ttk
# import sqlite3
# from venv import create
# global entries
# import subprocess

# create_table = """
# REATE TABLE IF NOT EXISTS movies (
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
#   FOREIGN KEY (director_id) REFERENCES directors(id),
#   FOREIGN KEY (genre_id) REFERENCES genres(id),
#   FOREIGN KEY (language_id) REFERENCES languages(id),
#   FOREIGN KEY (country_id) REFERENCES countries(id)
# );
# """
# insert_into = """
# INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description) VALUES
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
# """

# # Keeled
# create_table_keeled = """
# CREATE TABLE IF NOT EXISTS languages (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL
# );
# """

# create_table_riigid = """
# CREATE TABLE IF NOT EXISTS countries (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL
# );
# """

# create_table_žanrid = """
# CREATE TABLE IF NOT EXISTS genres (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL
# );
# """

# create_table_režissöörid = """
# CREATE TABLE IF NOT EXISTS directors (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL
# );
# """



# # this is for creating a new database because yes
# def create_table():
#     try:
#         conn = sqlite3.connect('moviesWORD.db')
#         cursor = conn.cursor()
#         print("Ühendus loodud")
#         # Siia päringud
#         cursor.execute(create_table)
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

# # Loo Tkinteri aken
# def load_data_from_db(tree):
#     # Loo ühendus SQLite andmebaasiga
#     conn = sqlite3.connect('moviesWORD.db')
#     cursor = conn.cursor()

#     # Tee päring andmebaasist andmete toomiseks
#     cursor.execute("SELECT title, director, release_year, genre, duration, rating, language, country, description FROM movies")
#     rows = cursor.fetchall()

#     # Lisa andmed tabelisse
#     for row in rows:
#         tree.insert("", "end", values=row)

#     # Sulge ühendus andmebaasiga
#     conn.close()

# def validate_data():
#     title = entries["Pealkiri"].get()
#     release_year = entries["Aasta"].get()
#     rating = entries["Reiting"].get()

#     if not title:
#         tk.messagebox.showerror("Viga", "Pealkiri on kohustuslik!")
#         return False
#     if not release_year.isdigit():
#         tk.messagebox.showerror("Viga", "Aasta peab olema arv!")
#         return False
#     if rating and (not rating.replace('.', '', 1).isdigit() or not (0 <= float(rating) <= 10)):
#         tk.messagebox.showerror("Viga", "Reiting peab olema vahemikus 0 kuni 10!")
#         return False

#     tk.messagebox.showinfo("Edu", "Andmed on kehtivad!")
#     return True

# def insert_data():
#     if validate_data():
#         connection = sqlite3.connect("moviesWORD.db")
#         cursor = connection.cursor()

#         cursor.execute("""
#             INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#         """, (
#             entries["Pealkiri"].get(),
#             entries["Režissöör"].get(),
#             entries["Aasta"].get(),
#             entries["Žanr"].get(),
#             entries["Kestus"].get(),
#             entries["Reiting"].get(),
#             entries["Keel"].get(),
#             entries["Riik"].get(),
#             entries["Kirjeldus"].get()
#         ))

#         connection.commit()
#         connection.close()
#         messagebox.showinfo("Edu", "Andmed sisestati edukalt!")
#         clear_entries()

# def clear_entries():
#     for entry in entries.values():
#         entry.delete(0, tk.END)

# def create_table():
#     try:
#         conn = sqlite3.connect('moviesWORD.db')
#         cursor = conn.cursor()
#         print("Ühendus loodud")
#         # Siia päringud
#         cursor.execute(create_table)
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

# def on_search():
#     search_query = search_entry.get()
#     load_data_from_db(tree, search_query)

# def add_data():
#     subprocess.run(["python", "01.py"])

# #Funktsioon, mis laadib andmed SQLite andmebaasist ja sisestab need Treeview tabelisse
# def load_data_from_db(tree, search_query=""):
#     # Puhasta Treeview tabel enne uute andmete lisamist
#     for item in tree.get_children():
#         tree.delete(item)

#     # Loo ühendus SQLite andmebaasiga
#     conn = sqlite3.connect('moviesWORD.db')
#     cursor = conn.cursor()

#     # Tee päring andmebaasist andmete toomiseks, koos ID-ga, kuid ID ei kuvata
#     if search_query:
#         cursor.execute("SELECT id, title, director, release_year, genre, duration, rating, language, country, description FROM movies WHERE title LIKE ?", ('%' + search_query + '%',))
#     else:
#         cursor.execute("SELECT id, title, director, release_year, genre, duration, rating, language, country, description FROM movies")

#     rows = cursor.fetchall()

#     # Lisa andmed tabelisse (Treeview), kuid ID-d ei kuvata
#     for row in rows:
#         tree.insert("", "end", values=row[1:], iid=row[0])  # iid määratakse ID-ks

#     # Sulge ühendus andmebaasiga
#     conn.close()


# # Loo sildid ja sisestusväljad
# entries = {}

# def lisa_andmed():
#     root = tk.Tk()
#     root.title("Filmid")
#     labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
#     for i, label in enumerate(labels):
#         tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
#         entry = tk.Entry(root, width=40)
#         entry.grid(row=i, column=1, padx=10, pady=5)
#         entries[label] = entry
#     # Loo nupp andmete sisestamiseks
#     submit_button = tk.Button(root, text="Sisesta andmed", command=insert_data)
#     submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)
#     root.mainloop

# def lisa_Keel():
#     def salvesta():
#         connection = sqlite3.connect("moviesWORD.db")
#         cursor = connection.cursor()
#         conn = sqlite3.connect('moviesWORD.db')
#         cursor = conn.cursor()
#         keel = entry_keel.get()
#         if keel:
#             cursor.execute("INSERT OR IGNORE INTO languages (name) VALUES (?)", (keel,))
#             conn.commit()
#             top.destroy()

#     top = Toplevel(root)
#     top.title("Lisa keel")
#     Label(top, text="Keel:").pack(pady=5)
#     entry_keel = Entry(top)
#     entry_keel.pack(pady=5)
#     Button(top, text="Salvesta", command=salvesta).pack(pady=10)

# def on_delete():
#     selected_item = tree.selection()  # Võta valitud rida
#     if selected_item:
#         record_id = selected_item[0]  # iid (ID)
#         confirm = messagebox.askyesno("Kinnita kustutamine", "Kas oled kindel, et soovid selle rea kustutada?")
#         if confirm:
#             try:
#                 # Loo andmebaasi ühendus
#                 conn = sqlite3.connect('moviesWORD.db')
#                 cursor = conn.cursor()
               
#                 # Kustuta kirje
#                 cursor.execute("DELETE FROM movies WHERE id=?", (record_id,))
#                 conn.commit()
#                 conn.close()
               
#                 # Värskenda Treeview tabelit
#                 load_data_from_db(tree)
               
#                 messagebox.showinfo("Edukalt kustutatud", "Rida on edukalt kustutatud!")
#             except sqlite3.Error as e:
#                 messagebox.showerror("Viga", f"Andmebaasi viga: {e}")
#     else:
#         messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")



# root = tk.Tk()
# root.title("Filmid")


# # Loo raam kerimisribaga
# frame = tk.Frame(root)
# frame.pack(pady=20, fill=tk.BOTH, expand=True)
# scrollbar = tk.Scrollbar(frame)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# # Loo tabel (Treeview) andmete kuvamiseks
# tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("title", "director", "year", "genre", "duration", "rating", "language", "country", "description"), show="headings")
# tree.pack(fill=tk.BOTH, expand=True)


# # Seosta kerimisriba tabeliga
# scrollbar.config(command=tree.yview)


# # Määra veergude pealkirjad ja laius
# tree.heading("title", text="Pealkiri")
# tree.heading("director", text="Režissöör")
# tree.heading("year", text="Aasta")
# tree.heading("genre", text="Žanr")
# tree.heading("duration", text="Kestus")
# tree.heading("rating", text="Reiting")
# tree.heading("language", text="Keel")
# tree.heading("country", text="Riik")
# tree.heading("description", text="Kirjeldus")

# tree.column("title", width=150)
# tree.column("director", width=100)
# tree.column("year", width=60)
# tree.column("genre", width=100)
# tree.column("duration", width=60)
# tree.column("rating", width=60)
# tree.column("language", width=80)
# tree.column("country", width=80)
# tree.column("description", width=200)

# # Lisa andmed tabelisse
# # tree.insert("", "end", values=("The Shawshank Redemption", "Frank Darabont", 1994, "Drama", 142, 9.3, "English", "USA", "Two imprisoned men bond over a number of years."))
# # tree.insert("", "end", values=("The Godfather", "Francis Ford Coppola", 1972, "Crime, Drama", 175, 9.2, "English", "USA", "The aging patriarch of an organized crime dynasty transfers control of his empire to his reluctant son."))
# # tree.insert("", "end", values=("The Dark Knight", "Christopher Nolan", 2008, "Action, Crime, Drama", 152, 9.0, "English", "USA", "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham."))
# load_data_from_db(tree)

# # Loo otsinguväli ja nupp
# search_frame = tk.Frame(root)
# search_frame.pack(pady=10)

# search_label = tk.Label(search_frame, text="Otsi filmi pealkirja järgi:")
# search_label.pack(side=tk.LEFT)

# search_entry = tk.Entry(search_frame)
# search_entry.pack(side=tk.LEFT, padx=10)

# search_button = tk.Button(search_frame, text="Otsi", command=on_search)
# search_button.pack(side=tk.LEFT)

# open_button = tk.Button(root, text="Lisa andmeid", command=lisa_andmed)
# open_button.pack(pady=20)

# delete_button = tk.Button(root, text="Kustuta", command=on_delete)
# delete_button.pack(pady=10)

# # Näita Tkinteri akent
# root.mainloop()


# import tkinter as tk
# from tkinter import Button, Entry, Label, Toplevel, messagebox
# from tkinter import ttk
# import sqlite3
# import subprocess

# # SQL for creating tables (example for movies table only here)
# create_table_movies = """
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
#   FOREIGN KEY (director_id) REFERENCES directors(id),
#   FOREIGN KEY (genre_id) REFERENCES genres(id),
#   FOREIGN KEY (language_id) REFERENCES languages(id),
#   FOREIGN KEY (country_id) REFERENCES countries(id)
# );
# """

# create_table_languages = """
# CREATE TABLE IF NOT EXISTS languages (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL
# );
# """

# create_table_countries = """
# CREATE TABLE IF NOT EXISTS countries (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL
# );
# """

# create_table_genres = """
# CREATE TABLE IF NOT EXISTS genres (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL
# );
# """

# create_table_directors = """
# CREATE TABLE IF NOT EXISTS directors (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE NOT NULL
# );
# """

# def initialize_database():
#     conn = sqlite3.connect('moviesWORD.db')
#     cursor = conn.cursor()
#     cursor.execute(create_table_languages)
#     cursor.execute(create_table_countries)
#     cursor.execute(create_table_genres)
#     cursor.execute(create_table_directors)
#     cursor.execute(create_table_movies)
#     conn.commit()
#     conn.close()

# # Clear entries dictionary on new form open
# entries = {}

# def validate_data():
#     title = entries["Pealkiri"].get()
#     release_year = entries["Aasta"].get()
#     rating = entries["Reiting"].get()

#     if not title:
#         messagebox.showerror("Viga", "Pealkiri on kohustuslik!")
#         return False
#     if not release_year.isdigit():
#         messagebox.showerror("Viga", "Aasta peab olema arv!")
#         return False
#     if rating and (not rating.replace('.', '', 1).isdigit() or not (0 <= float(rating) <= 10)):
#         messagebox.showerror("Viga", "Reiting peab olema vahemikus 0 kuni 10!")
#         return False

#     return True

# def get_or_create_id(cursor, table, name):
#     cursor.execute(f"SELECT id FROM {table} WHERE name = ?", (name,))
#     result = cursor.fetchone()
#     if result:
#         return result[0]
#     else:
#         cursor.execute(f"INSERT INTO {table} (name) VALUES (?)", (name,))
#         return cursor.lastrowid

# def insert_data():
#     if validate_data():
#         connection = sqlite3.connect("moviesWORD.db")
#         cursor = connection.cursor()

#         director_name = entries["Režissöör"].get()
#         genre_name = entries["Žanr"].get()
#         language_name = entries["Keel"].get()
#         country_name = entries["Riik"].get()

#         director_id = get_or_create_id(cursor, "directors", director_name) if director_name else None
#         genre_id = get_or_create_id(cursor, "genres", genre_name) if genre_name else None
#         language_id = get_or_create_id(cursor, "languages", language_name) if language_name else None
#         country_id = get_or_create_id(cursor, "countries", country_name) if country_name else None

#         # Convert duration and rating safely
#         duration = entries["Kestus"].get()
#         rating = entries["Reiting"].get()

#         cursor.execute("""
#             INSERT INTO movies (title, director_id, release_year, genre_id, duration, rating, language_id, country_id, description)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#         """, (
#             entries["Pealkiri"].get(),
#             director_id,
#             int(entries["Aasta"].get()),
#             genre_id,
#             int(duration) if duration.isdigit() else None,
#             float(rating) if rating else None,
#             language_id,
#             country_id,
#             entries["Kirjeldus"].get()
#         ))

#         connection.commit()
#         connection.close()
#         messagebox.showinfo("Edu", "Andmed sisestati edukalt!")
#         clear_entries()
#         load_data_from_db(tree)

# def clear_entries():
#     for entry in entries.values():
#         entry.delete(0, tk.END)

# def load_data_from_db(tree, search_query=""):
#     for item in tree.get_children():
#         tree.delete(item)

#     conn = sqlite3.connect('moviesWORD.db')
#     cursor = conn.cursor()

#     base_query = """
#     SELECT m.id, m.title, d.name AS director, m.release_year,
#            g.name AS genre, m.duration, m.rating,
#            l.name AS language, c.name AS country, m.description
#     FROM movies m
#     LEFT JOIN directors d ON m.director_id = d.id
#     LEFT JOIN genres g ON m.genre_id = g.id
#     LEFT JOIN languages l ON m.language_id = l.id
#     LEFT JOIN countries c ON m.country_id = c.id
#     """

#     if search_query:
#         cursor.execute(base_query + " WHERE m.title LIKE ?", ('%' + search_query + '%',))
#     else:
#         cursor.execute(base_query)

#     rows = cursor.fetchall()

#     for row in rows:
#         tree.insert("", "end", values=row[1:], iid=row[0])

#     conn.close()

# def on_search():
#     search_query = search_entry.get()
#     load_data_from_db(tree, search_query)

# def on_delete():
#     selected_item = tree.selection()
#     if selected_item:
#         record_id = selected_item[0]
#         confirm = messagebox.askyesno("Kinnita kustutamine", "Kas oled kindel, et soovid selle rea kustutada?")
#         if confirm:
#             try:
#                 conn = sqlite3.connect('moviesWORD.db')
#                 cursor = conn.cursor()
#                 cursor.execute("DELETE FROM movies WHERE id=?", (record_id,))
#                 conn.commit()
#                 conn.close()
#                 load_data_from_db(tree)
#                 messagebox.showinfo("Edukalt kustutatud", "Rida on edukalt kustutatud!")
#             except sqlite3.Error as e:
#                 messagebox.showerror("Viga", f"Andmebaasi viga: {e}")
#     else:
#         messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")

# def lisa_andmed():
#     add_window = tk.Toplevel(root)
#     add_window.title("Lisa film")

#     labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]

#     # Clear old entries dictionary before adding new widgets
#     entries.clear()

#     for i, label in enumerate(labels):
#         tk.Label(add_window, text=label).grid(row=i, column=0, padx=10, pady=5)
#         entry = tk.Entry(add_window, width=40)
#         entry.grid(row=i, column=1, padx=10, pady=5)
#         entries[label] = entry

#     submit_button = tk.Button(add_window, text="Sisesta andmed", command=insert_data)
#     submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

# # Initialize DB and GUI
# initialize_database()

# root = tk.Tk()
# root.title("Filmid")

# frame = tk.Frame(root)
# frame.pack(pady=20, fill=tk.BOTH, expand=True)

# scrollbar = tk.Scrollbar(frame)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set,
#                     columns=("title", "director", "year", "genre", "duration", "rating", "language", "country", "description"),
#                     show="headings")

# tree.pack(fill=tk.BOTH, expand=True)
# scrollbar.config(command=tree.yview)

# tree.heading("title", text="Pealkiri")
# tree.heading("director", text="Režissöör")
# tree.heading("year", text="Aasta")
# tree.heading("genre", text="Žanr")
# tree.heading("duration", text="Kestus")
# tree.heading("rating", text="Reiting")
# tree.heading("language", text="Keel")
# tree.heading("country", text="Riik")
# tree.heading("description", text="Kirjeldus")

# tree.column("title", width=150)
# tree.column("director", width=100)
# tree.column("year", width=60)
# tree.column("genre", width=100)
# tree.column("duration", width=60)
# tree.column("rating", width=60)
# tree.column("language", width=80)
# tree.column("country", width=80)
# tree.column("description", width=200)

# load_data_from_db(tree)

# search_frame = tk.Frame(root)
# search_frame.pack(pady=10)

# search_label = tk.Label(search_frame, text="Otsi filmi pealkirja järgi:")
# search_label.pack(side=tk.LEFT)

# search_entry = tk.Entry(search_frame)
# search_entry.pack(side=tk.LEFT, padx=10)

# search_button = tk.Button(search_frame, text="Otsi", command=on_search)
# search_button.pack(side=tk.LEFT)

# open_button = tk.Button(root, text="Lisa andmeid", command=lisa_andmed)
# open_button.pack(pady=20)

# delete_button = tk.Button(root, text="Kustuta", command=on_delete)
# delete_button.pack(pady=10)

# root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox, Toplevel, Label, Entry, Button, StringVar
import sqlite3

DB_NAME = "moviesWORD.db"

# Initialize DB & tables
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS languages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS directors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """)
    cursor.execute("""
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
    """)
    conn.commit()
    conn.close()

def get_conn():
    return sqlite3.connect(DB_NAME)

class MovieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Filmide andmebaas")

        # Columns for the treeview
        columns = ("title", "director", "year", "genre", "duration", "rating", "language", "country", "description")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Lisa film", command=self.open_add_movie).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Muuda film", command=self.open_edit_movie).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Kustuta film", command=self.delete_movie).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="Lisa režissöör", command=lambda: self.open_add_ref("directors")).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Lisa žanr", command=lambda: self.open_add_ref("genres")).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Lisa keel", command=lambda: self.open_add_ref("languages")).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Lisa riik", command=lambda: self.open_add_ref("countries")).pack(side=tk.LEFT, padx=5)

        self.load_movies()

    def load_movies(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.id, m.title, d.name, m.release_year, g.name, m.duration, m.rating, l.name, c.name, m.description
            FROM movies m
            LEFT JOIN directors d ON m.director_id = d.id
            LEFT JOIN genres g ON m.genre_id = g.id
            LEFT JOIN languages l ON m.language_id = l.id
            LEFT JOIN countries c ON m.country_id = c.id
            ORDER BY m.title
        """)
        for row in cursor.fetchall():
            movie_id = row[0]
            values = row[1:]
            self.tree.insert("", tk.END, iid=movie_id, values=values)
        conn.close()

    def open_add_movie(self):
        MovieForm(self, "Lisa film")

    def open_edit_movie(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Hoiatus", "Vali film, mida muuta!")
            return
        movie_id = selected[0]
        MovieForm(self, "Muuda filmi", movie_id)

    def delete_movie(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Hoiatus", "Vali film, mida kustutada!")
            return
        movie_id = selected[0]
        if messagebox.askyesno("Kinnita", "Kas oled kindel, et soovid selle filmi kustutada?"):
            conn = get_conn()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movies WHERE id=?", (movie_id,))
            conn.commit()
            conn.close()
            self.load_movies()
            messagebox.showinfo("Teade", "Film kustutatud")

    def open_add_ref(self, table_name):
        RefAddForm(self, table_name)

class MovieForm:
    def __init__(self, app, title, movie_id=None):
        self.app = app
        self.movie_id = movie_id
        self.top = Toplevel(app.root)
        self.top.title(title)

        labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
        self.entries = {}

        for i, label in enumerate(labels):
            ttk.Label(self.top, text=label).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)

        # Title Entry
        self.entries["Pealkiri"] = ttk.Entry(self.top, width=50)
        self.entries["Pealkiri"].grid(row=0, column=1, padx=5, pady=5)

        # ComboVars for foreign keys
        self.director_var = StringVar()
        self.genre_var = StringVar()
        self.language_var = StringVar()
        self.country_var = StringVar()

        # Director combobox
        self.entries["Režissöör"] = ttk.Combobox(self.top, textvariable=self.director_var)
        self.entries["Režissöör"].grid(row=1, column=1, padx=5, pady=5)
        self.entries["Režissöör"]['values'] = self.load_ref("directors")

        # Release Year Entry
        self.entries["Aasta"] = ttk.Entry(self.top, width=50)
        self.entries["Aasta"].grid(row=2, column=1, padx=5, pady=5)

        # Genre combobox
        self.entries["Žanr"] = ttk.Combobox(self.top, textvariable=self.genre_var)
        self.entries["Žanr"].grid(row=3, column=1, padx=5, pady=5)
        self.entries["Žanr"]['values'] = self.load_ref("genres")

        # Duration Entry
        self.entries["Kestus"] = ttk.Entry(self.top, width=50)
        self.entries["Kestus"].grid(row=4, column=1, padx=5, pady=5)

        # Rating Entry
        self.entries["Reiting"] = ttk.Entry(self.top, width=50)
        self.entries["Reiting"].grid(row=5, column=1, padx=5, pady=5)

        # Language combobox
        self.entries["Keel"] = ttk.Combobox(self.top, textvariable=self.language_var)
        self.entries["Keel"].grid(row=6, column=1, padx=5, pady=5)
        self.entries["Keel"]['values'] = self.load_ref("languages")

        # Country combobox
        self.entries["Riik"] = ttk.Combobox(self.top, textvariable=self.country_var)
        self.entries["Riik"].grid(row=7, column=1, padx=5, pady=5)
        self.entries["Riik"]['values'] = self.load_ref("countries")

        # Description Entry
        self.entries["Kirjeldus"] = ttk.Entry(self.top, width=50)
        self.entries["Kirjeldus"].grid(row=8, column=1, padx=5, pady=5)

        ttk.Button(self.top, text="Salvesta", command=self.save).grid(row=9, column=0, columnspan=2, pady=10)

        if movie_id:
            self.load_movie_data()

    def load_ref(self, table):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM {table} ORDER BY name")
        data = [row[0] for row in cursor.fetchall()]
        conn.close()
        return data

    def load_movie_data(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title, director_id, release_year, genre_id, duration, rating, language_id, country_id, description
            FROM movies WHERE id=?
        """, (self.movie_id,))
        movie = cursor.fetchone()
        conn.close()

        if movie:
            self.entries["Pealkiri"].insert(0, movie[0])
            self.entries["Režissöör"].set(self.get_name_by_id("directors", movie[1]))
            self.entries["Aasta"].insert(0, movie[2] if movie[2] else "")
            self.entries["Žanr"].set(self.get_name_by_id("genres", movie[3]))
            self.entries["Kestus"].insert(0, movie[4] if movie[4] else "")
            self.entries["Reiting"].insert(0, movie[5] if movie[5] else "")
            self.entries["Keel"].set(self.get_name_by_id("languages", movie[6]))
            self.entries["Riik"].set(self.get_name_by_id("countries", movie[7]))
            self.entries["Kirjeldus"].insert(0, movie[8] if movie[8] else "")

    def get_name_by_id(self, table, id_):
        if id_ is None:
            return ""
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM {table} WHERE id=?", (id_,))
        res = cursor.fetchone()
        conn.close()
        return res[0] if res else ""

    def get_id_by_name(self, table, name):
        if not name:
            return None
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(f"SELECT id FROM {table} WHERE name=?", (name,))
        res = cursor.fetchone()
        conn.close()
        return res[0] if res else None

    def save(self):
        title = self.entries["Pealkiri"].get().strip()
        if not title:
            messagebox.showerror("Viga", "Pealkiri on kohustuslik")
            return

        director_name = self.entries["Režissöör"].get()
        director_id = self.get_id_by_name("directors", director_name)

        genre_name = self.entries["Žanr"].get()
        genre_id = self.get_id_by_name("genres", genre_name)

        language_name = self.entries["Keel"].get()
        language_id = self.get_id_by_name("languages", language_name)

        country_name = self.entries["Riik"].get()
        country_id = self.get_id_by_name("countries", country_name)

        try:
            release_year = int(self.entries["Aasta"].get())
        except ValueError:
            release_year = None

        try:
            duration = int(self.entries["Kestus"].get())
        except ValueError:
            duration = None

        try:
            rating = float(self.entries["Reiting"].get())
        except ValueError:
            rating = None

        description = self.entries["Kirjeldus"].get().strip()

        conn = get_conn()
        cursor = conn.cursor()
        if self.movie_id:  # Update
            cursor.execute("""
                UPDATE movies SET
                title=?, director_id=?, release_year=?, genre_id=?, duration=?, rating=?, language_id=?, country_id=?, description=?
                WHERE id=?
            """, (title, director_id, release_year, genre_id, duration, rating, language_id, country_id, description, self.movie_id))
        else:  # Insert
            cursor.execute("""
                INSERT INTO movies (title, director_id, release_year, genre_id, duration, rating, language_id, country_id, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (title, director_id, release_year, genre_id, duration, rating, language_id, country_id, description))
            self.movie_id = cursor.lastrowid
        conn.commit()
        conn.close()

        self.app.load_movies()
        self.top.destroy()

class RefAddForm:
    def __init__(self, app, table_name):
        self.app = app
        self.table = table_name
        self.top = Toplevel(app.root)
        self.top.title(f"Lisa {table_name[:-1].capitalize()}")

        Label(self.top, text=f"{table_name[:-1].capitalize()}:").pack(pady=5)
        self.entry = Entry(self.top)
        self.entry.pack(pady=5)

        Button(self.top, text="Salvesta", command=self.save).pack(pady=10)

    def save(self):
        name = self.entry.get().strip()
        if not name:
            messagebox.showerror("Viga", "Nimi ei tohi olla tühi")
            return

        conn = get_conn()
        cursor = conn.cursor()
        try:
            cursor.execute(f"INSERT INTO {self.table} (name) VALUES (?)", (name,))
            conn.commit()
            messagebox.showinfo("Teade", f"{self.table[:-1].capitalize()} lisatud")
            self.app.load_movies()  # Reload movies to refresh comboboxes if needed
            self.top.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Viga", "Selline nimi on juba olemas")
        finally:
            conn.close()

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = MovieApp(root)
    root.mainloop()
