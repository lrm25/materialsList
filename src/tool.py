class ToolList:

    def __init__(self, table):
        self.table = table

    def add(self, name):
        if table.itemExists(name):
            print("Tool "+name+" already exists")
        else
            table.add_item(name)

    def get_all(self):

    def change_name(self, old_name, new_name):
        if not table.itemExists(old_name):
            print("No tool named "+name+" in table")
        else
            table.edit_item(old_name, new_name)

    def delete(self, name):
        if not table.itemExists(name):
            print("No tool named "+name+" in table")
        else
            table.delete_item(name)
            
