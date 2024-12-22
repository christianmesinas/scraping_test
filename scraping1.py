import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Fetch all books
cursor.execute('SELECT * FROM books')
books = cursor.fetchall()

for book in books:
    print(book)

conn.close()