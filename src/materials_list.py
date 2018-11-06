import sqlite3

EMPTY_OPTION_DICT="Options dictionary is empty"

from decision_tree import DecisionTree, retrieveAll

main_options = { "1" : "Generate materials list", \
                 "2" : "Create/edit tree", \
                 "3" : "Backup", \
                 "4" : "Quit" }

def main():
    while True:
        main_loop()

def select_option(option_dict, input_str, acceptable = ()):

    if option_dict is None or len(option_dict) is 0: 
        raise Exception(EMPTY_OPTION_DICT)
    option_selected = False
    for option in option_dict:
        print(option + ". " + option_dict[option])
    while not option_selected:
        selected_option = input(input_str)
        if not selected_option in acceptable and \
           not selected_option in option_dict:
            print("Invalid selection")
        else:
            option_selected = True
    return selected_option

def create_edit_tree():
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
    selected_option = select_option(retrieveAll(),
                                    "Select tree, or (c)reate new: ",
                                    ('c', 'C'))
    if selected_option.lower() == 'c':
        create_tree()

def create_tree():
    valid_tree = False
    tree_name = input("Enter tree name: ")
    tree = DecisionTree(tree_name)
    print("Created new tree with name " + tree.name)
    tree.store()
        
def generate_list():
    trees = retrieveAll()
    for tree_id in trees:
        print(str(tree_id) + ". " + trees[tree_id])
    selected_tree = input("Select tree: ")

def main_loop():
    selected_option = select_option(main_options, "Enter value: ")
    if selected_option == '1':
        generate_list()
    elif selected_option == '2':
        create_edit_tree()
    elif selected_option == '4':
        quit()
    else:
        print("Not implemented")
    #tree = DecisionTree()

if __name__ == "__main__":
    main()
