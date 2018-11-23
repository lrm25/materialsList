class ToolList:

    def __init__(self, table):
        self.table = table

    def add(self, name):
        if self.table.item_exists(name):
            print("Tool "+name+" already exists")
        else:
            self.table.add_item(name)

    def get_all(self):
        return self.table.get_all()

    def change_name(self, old_name, new_name):
        if not self.table.item_exists(old_name):
            print("No tool named "+name+" in table")
        else:
            self.table.edit_item(old_name, new_name)

    def delete(self, name):
        if not self.table.item_exists(name):
            print("No tool named "+name+" in table")
        else:
            self.table.delete_item(name)
            
