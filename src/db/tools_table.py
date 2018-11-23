
NAME = "tools"

class ToolsTable:

    def __init__(self, db):
        super().__init__(self, NAME, db)
        c = db.connect()
        try:
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND \
                  name='tools'")
            if (c.fetchone() is None):
                c.execute("CREATE TABLE tools (id int PRIMARY KEY, \
                          name text NOT NULL)")
            c.close()
        except sqlite3.Error as err:
            print("Error creating tools table:", err.args[0])

    def add_item(self, name):
        c = db.connect()
        c.execute("INSERT INTO tools (name) VALUE ?", (name,))

    def get_item(self, name):
        c = db.connect()
        c.execute("SELECT * FROM tools WHERE name=?", (name,))
        result = c.fetchone()
        c.close()
        return result

    def edit_item(self, old_name, new_name):
        c = db.connect()
        c.execute("UPDATE tools SET (name=?) WHERE name=?", (old_name,),
                  (new_name,))
        c.close()

    def delete_item(self, name):
        c = db.connect()
        c.execute("DELETE FROM tools WHERE name=?", (name,))
        c.close()

    def item_exists(self, name):
        result = get_item(name)
        return result is not None
