from DecisionTree import DecisionTree

main_options = { "1" : "Generate materials list", \
                 "2" : "Create/edit tree", \
                 "3" : "Backup", \
                 "4" : "Quit" }

existing_trees = { "1" : "Sample" }

def main():
    while True:
        main_loop()

def select_option(option_dict, input_str, acceptable = ()):
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
    selected_option = select_option(existing_trees,
                                    "Select tree, or (c)reate new: ",
                                    ('c', 'C'))
    if selected_option.lower() == 'c':
        create_tree()

def create_tree():
    valid_tree = False
    tree_name = input("Enter tree name: ")
    tree = DecisionTree(tree_name)
    print("Created new tree with name " + tree.name)
    existing_trees[str(len(existing_trees) + 1)] = tree.name
        
def generate_list():
    for tree in existing_trees:
        print(tree + ". " + existing_trees[tree])
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
