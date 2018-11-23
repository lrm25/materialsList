import sqlite3

from menu import *
from decision_tree import DecisionTree, retrieveAll

GEN_LIST = "1"
GEN_LIST_TEXT = "Generate materials list"
CE_TREE = "2"
CE_TREE_TEXT = "Create/edit tree"
TOOL_EDIT = "3"
TOOL_EDIT_TEXT = "Edit tools"
BACKUP = "4"
BACKUP_TEXT = "Backup"
QUIT = "5"
QUIT_TEXT = "Quit"

MAIN_OPTIONS = { GEN_LIST : GEN_LIST_TEXT, \
                 CE_TREE : CE_TREE_TEXT, \
                 TOOL_EDIT : TOOL_EDIT_TEXT, \
                 BACKUP : BACKUP_TEXT, \
                 QUIT : QUIT_TEXT }
INPUT_STR = "Enter value: "


class MainMenu(Menu):
    
    def __init__(self):
        super().__init__(MAIN_OPTIONS, INPUT_STR)

    def display(self):
        selected_option = super().select_option()
        print("Selected option: "+selected_option)
        if selected_option == GEN_LIST:
            self.generate_list()
        elif selected_option == CE_TREE:
            self.create_edit_tree()
        elif selected_option == QUIT:
            quit()
        else:
            print("Not implemented")

    def create_edit_tree(self):
        conn = sqlite3.connect("materialsList.db")
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND \
                  name='tree'")
        if (c.fetchone() is None):
            c.execute('''CREATE TABLE tree (id int, name text)''')
        c.execute('SELECT * FROM tree')
        if (c.fetchone() is None):
            sample_tree = DecisionTree('Sample')
            sample_tree.store()
        c.close()
        selected_option = self.select_option(retrieveAll(),
                                    "Select tree, create (n)ew, or (c)ancel: ",
                                    ('c', 'C', 'n', 'N'))
        if selected_option.lower() == 'n':
            self.create_tree()

    def create_tree(self):
        valid_tree = False
        tree_name = input("Enter tree name: ")
        tree = DecisionTree(tree_name)
        print("Created new tree with name " + tree.name)
        tree.store()
            
    def generate_list(self):
        trees = retrieveAll()
        #for tree_id in trees:
        #    print(str(tree_id) + ". " + trees[tree_id])
        #selected_tree = input("Select tree: ")
        selected_tree = self.select_option(trees, "Select tree or (c)ancel: ", \
                                      {'C', 'c'})

    def select_option(self, option_dict, input_str, acceptable = ()):

        if option_dict is None or len(option_dict) is 0: 
            raise Exception(EMPTY_OPTION_DICT)

        if input_str is None or len(input_str) is 0 or input_str.isspace():
            raise Exception(EMPTY_OPTION_STR)

        for also_allowed in acceptable:
            if also_allowed is None or len(also_allowed) is 0 or \
               also_allowed.isspace():
                raise Exception(INVALID_ACCEP_VAL)

        option_selected = False
        for option in option_dict:
            print(option + ". " + option_dict[option])

        while not option_selected:
            print(input_str, end=" ")
            selected_option = input()
            if not selected_option in acceptable and \
               not selected_option in option_dict:
                print(INVALID_SEL_STR)
            else:
                option_selected = True

        return selected_option

