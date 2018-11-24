from menu import Menu
from db.sqlite_db import DB
from db.tools_table import ToolsTable
from tool import ToolList

ADD_TOOL = "1"
ADD_TOOL_TEXT = "Add tool"
EDIT_TOOL = "2"
EDIT_TOOL_TEXT = "Rename tool"
DELETE_TOOL = "3"
DELETE_TOOL_TEXT = "Delete tool"
LIST_TOOLS = "4"
LIST_TOOLS_TEXT = "List tools"

TOOL_OPTIONS = { ADD_TOOL : ADD_TOOL_TEXT, \
                 EDIT_TOOL : EDIT_TOOL_TEXT, \
                 DELETE_TOOL : DELETE_TOOL_TEXT, \
                 LIST_TOOLS : LIST_TOOLS_TEXT }

INPUT_STR = "Select option, or (c)ancel:"

CANCEL_CHARS = ('C', 'c')

class ToolMenu(Menu):

    def __init__(self):
        super().__init__(TOOL_OPTIONS, INPUT_STR, CANCEL_CHARS)
        self._db = DB()
        self._tools_table = ToolsTable(self._db)
        self._tool_list = ToolList(self._tools_table)

    def display(self):
        selected_option = ""
        while(selected_option.lower() != 'c'):
            selected_option = super().select_option()
            if selected_option == ADD_TOOL:
                self.add_tool()
            elif selected_option == EDIT_TOOL:
                self.edit_tool()
            elif selected_option == DELETE_TOOL:
                self.delete_tool()
            elif selected_option == LIST_TOOLS:
                self.list_tools()

    def add_tool(self):
        tool_name = None
        while (tool_name is None) or tool_name.isspace():
            tool_name = input("Enter tool name: ")
            if tool_name.isspace():
                print("Tool name cannot be empty")  
            else:
                self._tool_list.add(tool_name)
                print(tool_name+" added to tool list")

    def edit_tool(self):
        self.list_tools()
        tool_name = None
        old_selected = False
        while not old_selected:
            tool_name = input("Enter tool name, or just ENTER to cancel: ")
            tool_name = tool_name.strip()
            if (not tool_name) or tool_name.isspace():
                break
            else:
                tool_info =self._tool_list.get(tool_name)
                if tool_info is None:
                    print("No tool named "+tool_name+" found")
                else:
                    old_selected = True
                    new_selected = False
                    while not new_selected:
                        new_name = input("Enter new name, or just \
                                         ENTER to cancel: ")
                        new_name = new_name.strip()
                        if (not new_name) or new_name.isspace():
                            break
                        elif self._tool_list.get(new_name) is not None:
                            print("Tool with name "+new_name+" already exists")
                        else:
                            self._tool_list.change_name(tool_name, new_name)
                            new_selected = True

    def delete_tool(self):
        self.list_tools()
        deleted = False
        while not deleted:
            tool_name = input("Enter tool name, or just ENTER to cancel: ")
            tool_name = tool_name.strip()
            if (not tool_name) or tool_name.isspace():
                break
            else:
                tool_info = self._tool_list.get(tool_name)
                if tool_info is None:
                    print("No tool named "+tool_name+" found")
                else:
                    self._tool_list.delete(tool_name)
                    deleted = True

    def list_tools(self):
        for tool in self._tool_list.get_all():
            print(tool)
