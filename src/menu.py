EMPTY_OPTION_DICT="Options dictionary is empty"
EMPTY_OPTION_STR="Empty option selection string"
INVALID_ACCEP_VAL="Invalid additional option"
INVALID_SEL_STR="Invalid selection"

class Menu:

    def __init__(self, option_dict, input_str, acceptable = ()):
        self.option_dict = option_dict
        self.input_str = input_str
        self.acceptable = acceptable

    def select_option(self):

        if self.option_dict is None or len(self.option_dict) is 0: 
            raise Exception(EMPTY_OPTION_DICT)

        if self.input_str is None or len(self.input_str) is 0 or \
           self.input_str.isspace():
            raise Exception(EMPTY_OPTION_STR)

        for also_allowed in self.acceptable:
            if also_allowed is None or len(also_allowed) is 0 or \
               also_allowed.isspace():
                raise Exception(INVALID_ACCEP_VAL)

        option_selected = False
        for option in self.option_dict:
            print(option + ". " + self.option_dict[option])

        while not option_selected:
            print(self.input_str, end=" ")
            selected_option = input()
            if not selected_option in self.acceptable and \
               not selected_option in self.option_dict:
                print(INVALID_SEL_STR)
            else:
                option_selected = True

        return selected_option 
