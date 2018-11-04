from DecisionTree import DecisionTree

main_options = { "1" : "Generate materials list", \
                 "2" : "Create/edit tree", \
                 "3" : "Backup", \
                 "4" : "Quit" }

existing_trees = { "1" : "Sample" }

def main():
    while True:
        main_loop()

def create_edit_tree():
    option_selected = False
    for option in existing_trees:
        print(option + ". " + existing_trees[option])
    while not option_selected:
        selected_option = input("Select tree, or (c)reate new:  ")
        if selected_option.lower() != 'c' and \
           not selected_option in existing_trees:
            print("Invalid selection")
        else:
            option_selected = True
    if selected_option.lower() == 'c':
        create_tree()

def create_tree():
    valid_tree = False
    tree_name = input("Enter tree name: ")
    tree = DecisionTree(tree_name)
    print("Created new tree with name " + tree.name)
        

def main_loop():
    option_selected = False
    for option in main_options:
        print(option + ". " + main_options[option])
    while not option_selected:
        selected_option = input("Enter value: ")
        if not selected_option in main_options:
            print("Invalid selection")
        else:
            option_selected = True
    if selected_option == '2':
        create_edit_tree()
    elif selected_option == '4':
        quit()
    else:
        print("Not implemented")
    #tree = DecisionTree()

if __name__ == "__main__":
    main()
