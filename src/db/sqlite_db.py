import sqlite3

cursor=

class DB:

    def add_table(self, table):

    def connect(self, db_name="materialsList.db"):
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
        except sqlite3.Error as err:
            print("Error connecting to database %s:  %s" % (db_name, err))
        return cursor

    def get_tools_table():
        if self.tools_table is None:
            self.tools_table = ToolsTable(self)
        return self.tools_table

    def initialize_schema():
        c.execute("CREATE TABLE tree (id int PRIMARY KEY, name text, 
                  questions text)")

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
