# import the sqlite3 module into python
import sqlite3

# connect to books.db database or create if its not there already
db = sqlite3.connect('books.db')

# create a cursor in the database
cur = db.cursor()

# create table if its not there already using SQL Commands
cur.execute ('''CREATE TABLE IF NOT EXISTS books(
    id integer PRIMARY KEY,
    title text NOT NULL,
    author text NOT NULL,
    price real);''')

# add a data entry into the database table
cur.execute('''INSERT INTO books(id, title, author, price)
    VALUES('1','Human Compatible: AI and the Problem of Control','Stuart Russell','7.99')''')

# list of books to add to the database
book_list = [('2','The Art of Statistics: Learning from Data','David Spiegelhalter','8.19'),
             ('3','Factfulness: Ten Reasons Were Wrong About The World - And Why Things Are Better Than You Think','Hans Rosling','7.20'),
             ('4','Life 3.0: Being Human in the Age of Artificial Intelligence','Max Tegmark','7.69'),
             ('5','Superintelligence: Paths, Dangers, Strategies','Nick Bostrom','8.19'),
             ('6','Thinking, Fast and Slow','Daniel Kahneman','8.99'),
             ('7','Sapiens: A Brief History of Humankind','Yuval Noah Harari','7.99'),
            ]

# add multiple data entry into the database table
cur.executemany('''INSERT INTO books(id, title, author, price)
    VALUES(?,?,?,?)''',book_list)

# run an SQL query to look at the list of books in the database and print the results on screen
cur.execute('SELECT * FROM books')
print(cur.fetchall())

# commit to the database
db.commit()

# close the database
db.close()
