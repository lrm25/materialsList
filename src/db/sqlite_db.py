import sqlite3

cursor=

class DB:

    def connect(db_name="materialsList.db"):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        return cursor

    def initialize_schema():
        c.execute("CREATE TABLE tree (id int, name text, questions text)")

    def get_trees():

        trees = {}

        cursor = connect()
        for row in cursor.execute('SELECT * FROM tree'):
            trees[str(row[0])] = row[1]
        cursor.close()
        return trees
        
    def tree_exists(name):
        
        c = connect()
        c.execute("SELECT * FROM tree where name=?", (name,))
        return (c.fetchone() is not None

    def add_tree(name):
        
        c = connect()
        c.execute('SELECT Count(*) FROM tree')
        c.execute('INSERT INTO tree VALUES (?, ?, ?)', 
