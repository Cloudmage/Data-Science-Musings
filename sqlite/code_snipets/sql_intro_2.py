# import the sqlite3 module into python
import sqlite3

# connect to books.db database or create if its not there already
db = sqlite3.connect('books.db')

# create a cursor in the database
cur = db.cursor()

# run an SQL query to select all books in order of title
cur.execute('SELECT * FROM books ORDER BY title')

# Use a for loop to print out each book on a new line
for x in cur.fetchall():
    print(x)

# run an SQL query to select books where the price is greater than 8
cur.execute('SELECT * FROM books WHERE price >8')

# put a line on the screen to seperate the data output
print('**************')

# Use a for loop to print out each book on a new line
for x in cur.fetchall():
    print(x)

# put a line on the screen to seperate the data output
print('**************')

# run an SQL query to select all from Author and print to the screen
cur.execute('SELECT author FROM books')
print(cur.fetchall())

# close the database
db.close()
