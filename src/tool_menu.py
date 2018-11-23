from menu import Menu
from db.sqlite_db import DB
from db.tools_table import ToolsTable
from tool import ToolList

ADD_TOOL = "1"
ADD_TOOL_TEXT = "Add tool"
LIST_TOOLS = "2"
LIST_TOOLS_TEXT = "List tools"

TOOL_OPTIONS = { ADD_TOOL : ADD_TOOL_TEXT, \
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

    def list_tools(self):
        for tool in self._tool_list.get_all():
            print(tool)
