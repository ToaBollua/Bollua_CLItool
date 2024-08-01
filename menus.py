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

        if opt == "1" or opt == "01":
            os.system("clear")
            banner.test()
            self.pentest_menu()
        elif opt == "2" or opt == "02":
            os.system("clear")
            banner.test()
            self.calculation_menu()
        elif opt == "3" or opt == "03":
            os.system("clear")
            banner.test()
            self.utility_menu()
        elif opt == "0" or opt == "00":
            os.system("clear")
            banner.test()
            print("Exiting...")
            time.sleep(1)
            exit()
        else:
            print("Invalid option, please try again.")
            self.main_menu()

    def return_to_menu(self, menu):
        input("Press Enter to return to the menu...")
        menu()

    def pentest_menu(self):
        print("These are the available tools in this CLI:\n")
        time.sleep(1)
        print("01) sqlmap - SQL injection detection and exploitation tool")
        print("02) pagodo - Google-based web vulnerability scanner")
        print("03) EmailAll - Advanced email collection tool")
        print("00) Return to menu.")

        tool_opt = input("Select a tool to install or run>> ")

        if tool_opt == "1" or tool_opt == "01" or tool_opt == "sqlmap":
            self.tool_installer.install_tool("sqlmap")
            run_tool(self.base_path, self.python_command, "sqlmap", self.pentest_menu)

        elif tool_opt == "2" or tool_opt == "02" or tool_opt == "pagodo":
            self.tool_installer.install_tool("pagodo")
            run_tool(self.base_path, self.python_command, "pagodo", self.pentest_menu)

        elif (
            tool_opt == "3"
            or tool_opt == "03"
            or tool_opt == "EmailAll"
            or tool_opt == "emailall"
        ):
            self.tool_installer.install_tool("emailall")
            run_tool(self.base_path, self.python_command, "emailall", self.pentest_menu)

        elif tool_opt == "00" or tool_opt == "0" or tool_opt == "back":
            self.return_to_menu(self.main_menu)

        else:
            print("\nPlease select a valid input, returning now.\n")
            self.return_to_menu(self.main_menu)

    def calculation_menu(self):
        print("These are the available tools:\n")
        time.sleep(1)
        print("01) calculator - Simple CLI calculator")
        print("02) IMC - IMC calculator")
        print("03) watch - It gives time...")
        print("00) Return to menu")

        tool_opt = input("Select a tool to install or run>> ")

        if tool_opt == "01" or tool_opt == "1" or tool_opt.lower() == "calculator":
            self.tool_installer.install_tool("calculator")
            run_tool(self.base_path, self.python_command, "calculator", self.calculation_menu)

        elif tool_opt == "02" or tool_opt == "2" or tool_opt.lower() == "imc":
            self.tool_installer.install_tool("IMC")
            run_tool(self.base_path, self.python_command, "IMC", self.calculation_menu)

        elif tool_opt == "03" or tool_opt == "3" or tool_opt.lower() == "watch":
            self.tool_installer.install_tool("watch")
            run_tool(self.base_path, self.python_command, "watch", self.calculation_menu)

        elif tool_opt == "00" or "0" or "back":
            self.return_to_menu(self.main_menu)

        else:
            print("\nPlease select a valid input, returning now.\n")
            self.return_to_menu(self.main_menu)
