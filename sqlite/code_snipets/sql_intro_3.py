# this script requires pandas to be preinstalled
# pip install pandas

# import the sqlite3 and pandas modules into python
import sqlite3
import pandas as pd

# connect to books.db database or create if its not there already
db = sqlite3.connect('books.db')

# read the data from the SQL database into a Pandas dataframe
data = pd.read_sql_query('SELECT * FROM books;', db)

# show top 5 rows
print (data.head())

# put a line on the screen to seperate the data output
print('**************')

# print the entire dataframe to the screen
print(data)

# put a line on the screen to seperate the data output
print('**************')

# add a new row to the dataframe
new_row = {'id':'8','author':'Professor Shoshana Zuboff','title':'The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power','price':'8.99'}

# append the row to the dataframe
data = data.append(new_row, ignore_index=True)

# print the entire dataframe to the screen
print(data)

# Add the new row to the Database
data.to_sql('books',db, if_exists='replace', index=False)
