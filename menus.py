"""

 __    __     ______     __   __     __  __     ______    
/\ "-./  \   /\  ___\   /\ "-.\ \   /\ \/\ \   /\  ___\   
\ \ \-./\ \  \ \  __\   \ \ \-.  \  \ \ \_\ \  \ \___  \  
 \ \_\ \ \_\  \ \_____\  \ \_\\"\_\  \ \_____\  \/\_____\ 
  \/_/  \/_/   \/_____/   \/_/ \/_/   \/_____/   \/_____/ 
                                                          

Here are the menus of the toolkit
categorized by functionality.

Here we also call the corresponding
tool functions.

You can add your tools
(specified in tools.py) and custom
menus here!

~ Bollua

"""

import os
import time
import banner
from tools_installer import ToolInstaller
from runners import run_tool
from tools import tools

class Menu:
    def __init__(self, base_path, python_command):
        self.base_path = base_path
        self.python_command = python_command
        self.tool_installer = ToolInstaller(base_path)

    def main_menu(self):
        os.system("clear")
        banner.test()
        print("Welcome to the main menu!")
        time.sleep(1)
        print("01) Penetration Testing Tools")
        print("02) Calculation Tools")
        print("03) Utility Tools")
        print("00) Exit")

        opt = input("Select an option>> ")

        options = {
            "1": self.pentest_menu,
            "2": self.calculation_menu,
            "3": self.utility_menu,
            "0": self.exit
        }

        if opt in options:
            os.system("clear")
            banner.test()
            options[opt]()
        else:
            print("Invalid option, please try again.")
            self.main_menu()
    
    def return_to_menu(self, menu):
        os.system("clear")
        banner.test()
        menu()

    def display_tools_and_handle_selection(self, category, menu):
        self.display_tools(category)
        self.handle_tool_selection(category, menu)

    def pentest_menu(self):
        self.display_tools_and_handle_selection("pentest", self.pentest_menu)

    def calculation_menu(self):
        self.display_tools_and_handle_selection("calculation", self.calculation_menu)

    def utility_menu(self):
        self.display_tools_and_handle_selection("utility", self.utility_menu)

    def display_tools(self, category):
        print("These are the available tools in this CLI:\n")
        time.sleep(1)
        tool_info = tools.get(category)
        if tool_info:
            for i, (tool_name, tool_data) in enumerate(tool_info.items(), start=1):
                print(f"{i:02}) {tool_data['name']} - {tool_data['description']}")
        else:
            print(f"No tools found in category '{category}'")
        print("00) Return to menu")

    def handle_tool_selection(self, category, menu):
        tool_opt = input("Select a tool to install or run>> ")

        if tool_opt in ["00", "0", "back"]:
            self.return_to_menu(self.main_menu)
        elif tool_opt.isdigit() and 1 <= int(tool_opt) <= len(tools[category]):
            tool_key = list(tools[category].keys())[int(tool_opt) - 1]
            self.tool_installer.install_tool(category, tool_key)
            run_tool(self.base_path, self.python_command, category, tool_key)
        else:
            print("\nPlease select a valid input, returning now.\n")
            self.return_to_menu(menu)

    def exit(self):
        os.system("clear")
        banner.test()
        print("Exiting...")
        time.sleep(1)
        exit()