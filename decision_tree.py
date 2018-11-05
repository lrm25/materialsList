import sqlite3

from Question import Question

def retrieve(tree_id, dbpath="materialsList.db"):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    t_id = (tree_id,)
    c.execute('SELECT * FROM tree WHERE id=?', t_id)
    c.close()

def retrieveAll(dbpath="materialsList.db"):

    trees = {}

    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND \
              name='tree'")
    if(c.fetchone() is not None):
        for row in c.execute('SELECT * FROM tree'):
            ids = row[0]
            trees[str(row[0])] = row[1]
    c.close()
    return trees

class DecisionTree:

    def __init__(self, name, tree_id=0):
        self.id = tree_id
        self.name = name
        #self.main_question = Question(1, "What do you want out of life?", \
        #                              ("Nothing", "Everything"))
        #self.main_question.ask()
        #self.main_question.get_answer()

    def store(self, dbpath="materialsList.db"):
        conn = sqlite3.connect(dbpath)
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND \
                  name='tree'")
        if (c.fetchone() is None):
            c.execute('''CREATE TABLE tree (id int, name text)''')
        c.execute('SELECT * FROM tree')
        self.tree_id = len(c.fetchall()) + 1
        t_info = (self.tree_id, self.name)
        c.execute('INSERT INTO tree VALUES (?, ?)', t_info)
        conn.commit()
        conn.close()
