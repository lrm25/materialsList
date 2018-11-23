from db.table import Table

NAME = "tools"

class ToolsTable(Table):


    def __init__(self, db):
        super().__init__(NAME, db)
        c = db.connect()
        try:
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND \
                  name='tools'")
            if (c.fetchone() is None):
                c.execute("CREATE TABLE tools (id INTEGER PRIMARY KEY, \
                          name TEXT NOT NULL)")
            c.close()
        except sqlite3.Error as err:
            print("Error creating tools table:", err.args[0])

    def add_item(self, name):
        c = self.db.connect()
        c.execute('''INSERT INTO tools(name) VALUES(?)''', (name,))
        self.db.commit()
        print(c.lastrowid)
        print("Insertion complete: " + name)
        c.close()

    def get_item(self, name):
        c = self.db.connect()
        c.execute('''SELECT * FROM tools WHERE name=?''', (name,))
        result = c.fetchone()
        c.close()
        return result

    def get_all(self):
        tools_list = []
        c = self.db.connect()
        c.execute('''SELECT * FROM tools''')
        for result in c.fetchall():
            tools_list.append(result[1])
        return tools_list
            

    def edit_item(self, old_name, new_name):
        c = self.db.connect()
        c.execute("UPDATE tools SET (name=?) WHERE name=?", (old_name,),
                  (new_name,))
        c.close()

    def delete_item(self, name):
        c = self.db.connect()
        c.execute("DELETE FROM tools WHERE name=?", (name,))
        c.close()

    def item_exists(self, name):
        result = self.get_item(name)
        return result is not None
