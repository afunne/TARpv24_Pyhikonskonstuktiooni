import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
global entries
import subprocess

create_table = """
 CREATE TABLE IF NOT EXISTS movies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  director TEXT,
  release_year INTEGER,
  genre TEXT,
  duration INTEGER,
  rating REAL,
  language TEXT,
  country TEXT,
  description TEXT
);
"""
insert_into = """
INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description) VALUES
('The From In With.', 'Francis Ford Coppola', 1994, 'Drama', 142, 9.3, 'English', 'USA', 'The In With By On. A In From By The At. On A With By By On To A.'),
('The By On To.', 'Christopher Nolan', 2010, 'Sci-Fi', 148, 8.8, 'English', 'UK', 'The A The On The In. By To A At On The. From The In With At In To A.'),
('In The With On.', 'Quentin Tarantino', 1972, 'Crime', 175, 9.2, 'English', 'USA', 'On From The By At The A. In From By With To On. A The By In With At On To A.'),
('The A To From.', 'Steven Spielberg', 1994, 'Adventure', 154, 8.9, 'English', 'France', 'With By In The A On. The With To A At The From. On A From With At By The.'),
('On The From With.', 'Martin Scorsese', 2008, 'Action', 152, 9.0, 'English', 'Germany', 'The A By On In The. At With To A From On The. With On By The A In To From.'),
('From The By With.', 'Christopher Nolan', 1960, 'Drama', 134, 8.5, 'English', 'UK', 'The A On From The At. With To By In A The On. At The In From With By To A.'),
('The By On A.', 'Francis Ford Coppola', 1999, 'Thriller', 112, 7.8, 'English', 'USA', 'A The On By In The At. From With A On By To The. In The By With At A From.'),
('On A The From.', 'Quentin Tarantino', 2015, 'Comedy', 126, 7.9, 'English', 'Italy', 'By With A On In The From. The By At A With On To. At In The By From With A.'),
('By The On From.', 'Steven Spielberg', 1975, 'Action', 143, 8.7, 'English', 'France', 'A With On The By From In. The A At On With To From. By In The A From With At On.'),
('From With The By.', 'Martin Scorsese', 1980, 'Crime', 163, 9.1, 'English', 'Germany', 'On The A By In The From. With By On A The In From. To The In At By With On A.');
"""

# Loo Tkinteri aken
def load_data_from_db(tree):
    # Loo ühendus SQLite andmebaasiga
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Tee päring andmebaasist andmete toomiseks
    cursor.execute("SELECT title, director, release_year, genre, duration, rating, language, country, description FROM movies")
    rows = cursor.fetchall()

    # Lisa andmed tabelisse
    for row in rows:
        tree.insert("", "end", values=row)

    # Sulge ühendus andmebaasiga
    conn.close()

def validate_data():
    title = entries["Pealkiri"].get()
    release_year = entries["Aasta"].get()
    rating = entries["Reiting"].get()

    if not title:
        tk.messagebox.showerror("Viga", "Pealkiri on kohustuslik!")
        return False
    if not release_year.isdigit():
        tk.messagebox.showerror("Viga", "Aasta peab olema arv!")
        return False
    if rating and (not rating.replace('.', '', 1).isdigit() or not (0 <= float(rating) <= 10)):
        tk.messagebox.showerror("Viga", "Reiting peab olema vahemikus 0 kuni 10!")
        return False

    tk.messagebox.showinfo("Edu", "Andmed on kehtivad!")
    return True

def insert_data():
    if validate_data():
        connection = sqlite3.connect("movies.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            entries["Pealkiri"].get(),
            entries["Režissöör"].get(),
            entries["Aasta"].get(),
            entries["Žanr"].get(),
            entries["Kestus"].get(),
            entries["Reiting"].get(),
            entries["Keel"].get(),
            entries["Riik"].get(),
            entries["Kirjeldus"].get()
        ))

        connection.commit()
        connection.close()
        messagebox.showinfo("Edu", "Andmed sisestati edukalt!")
        clear_entries()

def clear_entries():
    for entry in entries.values():
        entry.delete(0, tk.END)

def create_table():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Ühendus loodud")
        # Siia päringud
        cursor.execute(create_table)
        print("Tabel loodud")

    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel:", error)
    finally:
        if conn:
            conn.close()

def insert():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        cursor.execute(insert_into)
        print("Tebel täidetud")

    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel:", error)
    finally:
        if conn:
            conn.close()

def täida_tabel():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Ühendus loodud")

        # Teostame päringu, et lugeda kõik andmed tabelist 'movies'
        cursor.execute("SELECT * FROM movies")
        rows = cursor.fetchall() # shows result in the screen

        # Väljastame kõik loetud read
        for row in rows:
            print(row)

    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel või päringu teostamisel:", error)
    finally:
        if conn:
            conn.close()
            print("Ühendus suleti")

def on_search():
    search_query = search_entry.get()
    load_data_from_db(tree, search_query)

def add_data():
    subprocess.run(["python", "01.py"])

#Funktsioon, mis laadib andmed SQLite andmebaasist ja sisestab need Treeview tabelisse
def load_data_from_db(tree, search_query=""):
    # Puhasta Treeview tabel enne uute andmete lisamist
    for item in tree.get_children():
        tree.delete(item)

    # Loo ühendus SQLite andmebaasiga
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Tee päring andmebaasist andmete toomiseks, koos ID-ga, kuid ID ei kuvata
    if search_query:
        cursor.execute("SELECT id, title, director, release_year, genre, duration, rating, language, country, description FROM movies WHERE title LIKE ?", ('%' + search_query + '%',))
    else:
        cursor.execute("SELECT id, title, director, release_year, genre, duration, rating, language, country, description FROM movies")

    rows = cursor.fetchall()

    # Lisa andmed tabelisse (Treeview), kuid ID-d ei kuvata
    for row in rows:
        tree.insert("", "end", values=row[1:], iid=row[0])  # iid määratakse ID-ks

    # Sulge ühendus andmebaasiga
    conn.close()


# Loo sildid ja sisestusväljad
entries = {}

def lisa_andmed():
    root = tk.Tk()
    root.title("Filmid")
    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
    for i, label in enumerate(labels):
        tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(root, width=40)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry
    # Loo nupp andmete sisestamiseks
    submit_button = tk.Button(root, text="Sisesta andmed", command=insert_data)
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)
    root.mainloop

root = tk.Tk()
root.title("Filmid")


# Loo raam kerimisribaga
frame = tk.Frame(root)
frame.pack(pady=20, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# Loo tabel (Treeview) andmete kuvamiseks
tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("title", "director", "year", "genre", "duration", "rating", "language", "country", "description"), show="headings")
tree.pack(fill=tk.BOTH, expand=True)


# Seosta kerimisriba tabeliga
scrollbar.config(command=tree.yview)


# Määra veergude pealkirjad ja laius
tree.heading("title", text="Pealkiri")
tree.heading("director", text="Režissöör")
tree.heading("year", text="Aasta")
tree.heading("genre", text="Žanr")
tree.heading("duration", text="Kestus")
tree.heading("rating", text="Reiting")
tree.heading("language", text="Keel")
tree.heading("country", text="Riik")
tree.heading("description", text="Kirjeldus")

tree.column("title", width=150)
tree.column("director", width=100)
tree.column("year", width=60)
tree.column("genre", width=100)
tree.column("duration", width=60)
tree.column("rating", width=60)
tree.column("language", width=80)
tree.column("country", width=80)
tree.column("description", width=200)

# Lisa andmed tabelisse
# tree.insert("", "end", values=("The Shawshank Redemption", "Frank Darabont", 1994, "Drama", 142, 9.3, "English", "USA", "Two imprisoned men bond over a number of years."))
# tree.insert("", "end", values=("The Godfather", "Francis Ford Coppola", 1972, "Crime, Drama", 175, 9.2, "English", "USA", "The aging patriarch of an organized crime dynasty transfers control of his empire to his reluctant son."))
# tree.insert("", "end", values=("The Dark Knight", "Christopher Nolan", 2008, "Action, Crime, Drama", 152, 9.0, "English", "USA", "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham."))
load_data_from_db(tree)

# Loo otsinguväli ja nupp
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Otsi filmi pealkirja järgi:")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Otsi", command=on_search)
search_button.pack(side=tk.LEFT)

open_button = tk.Button(root, text="Lisa andmeid", command=lisa_andmed)
open_button.pack(pady=20)

# Näita Tkinteri akent
root.mainloop()
