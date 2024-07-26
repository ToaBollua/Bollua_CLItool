"""



 █     █░ ▄▄▄       ██▀███   ███▄    █  ██▓ ███▄    █   ▄████  ▐██▌  ▐██▌  ▐██▌ 
▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █  ██▒ ▀█▒ ▐██▌  ▐██▌  ▐██▌ 
▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░ ▐██▌  ▐██▌  ▐██▌ 
░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒░▓█  ██▓ ▓██▒  ▓██▒  ▓██▒ 
░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒▒██░   ▓██░░██░▒██░   ▓██░░▒▓███▀▒ ▒▄▄   ▒▄▄   ▒▄▄  
░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒  ░▀▀▒  ░▀▀▒  ░▀▀▒ 
  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░  ░   ░  ░  ░  ░  ░  ░  ░ 
  ░   ░    ░   ▒     ░░   ░    ░   ░ ░  ▒ ░   ░   ░ ░ ░ ░   ░     ░     ░     ░ 
    ░          ░  ░   ░              ░  ░           ░       ░  ░     ░     ░    
                                                                                


THIS BRANCH OF THE SCRIPT IS STILL A WORK IN PROGRESS!!!
IT IS ALSO DESIGNED TO WORK MAINLY ON LINUX!

THIS MAIN.PY FILE IS NOT DONE. IT NEEDS MORE WORK
TO BE DONE BEFORE IT CAN BE USED AS A MAIN SCRIPT

YOU CANNOT ACTUALLY RUN THIS SCRIPT ON IT'S
CURRENT STATE SINCE THIS EXACT VERSION HAS
UNFINISHED CHANGES.

I AM CURRENTLY WORKING ON MODULARIZE THE FUNCTIONS
FOR THE TOOLS SO ITS EASIER TO UPSCALE
AND ADMINISTER IN THE FUTURE, ALSO MAKING IT
SOMEWHAT CUSTOMIZABLE FOR USERS THAT MIGHT WANNA
FORK THIS REPO AND WORK ON YOUR OWN TOOLKITS!

THANKS FOR READING AND FOR YOUR INTEREST IN MY
PROJECT! :D

~ Bollua

"""

__author__ = "Bollua"
__python_version__ = "3.12.4"

# IMPORTS SCRIPT'S DEPENDENCIES
try:
    import sys
    import os
    import subprocess
    import time
    import shutil
    import platform
    import banner
    import tools
except ModuleNotFoundError as e:
    print("Module not found, please check installation: {e}")
    quit()


# This sets the program's path

script_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_path)
home_dir = os.path.expanduser("~")
cli_tool_dir = os.path.join(home_dir, "CLItool")
path = os.environ["PATH"]
if cli_tool_dir not in path:
    os.environ["PATH"] = cli_tool_dir + os.pathsep + path


# HERE GOES THE TOOLS GITHUB LINK
class clitool:
    def __init__(self):

        # THIS SETS YOUR DEFAULT PYTHON COMMAND AFTER CHECKING
        self.python_command = self.get_python_command()


    def check_git_installation(self, menu):
        if shutil.which("git") is None:
            self.git_opt = input(
                "git is not installed. Do you want to install git?\n(Y/N)>> "
            )
            if self.git_opt == "Y" or self.git_opt == "y":
                print("===== Installing git... =====\n")
                if platform.system() == "Windows":
                    os.system("winget install --id Git.Git")
                elif platform.system() == "Darwin":  # macOS
                    os.system("brew install git")
                else:  # Linux
                    os.system(
                        "sudo pacman -S install git"
                    )  # or yum, zypper, etc. depending on the distro
                print("===== Done! =====")
            elif self.git_opt == "N" or self.git_opt == "n":
                print("Oh then fuck you...")
                self.return_to_menu(menu)
            else:
                print("Please insert a valid option! Exiting now. . .")
                time.sleep(3)
                os.system("clear")
                banner.test()
                return

    # THIS CHECKS WHICH PYTHON COMMAND IS USED IN THE USER'S MACHINE AND USES THAT TO OPEN OTHER PYTHON FILES
    def get_python_command(self):
        if shutil.which("py") is not None:
            return "py"
        elif shutil.which("python") is not None:
            return "python"
        elif shutil.which("python3") is not None:
            return "python3"
        else:
            print(
                "Python is not installed. Please install python and try again.\n===== RECOMMENDED VERSION 3.11.8 ====="
            )

    def return_to_menu(self, menu):
        print("Returning to main menu...")
        os.system("clear")
        time.sleep(1)
        banner.test()
        self.menu()


    # HERE WE DISPLAY THE UTILITY TOOLS MENU
    def utility_menu(self):
        print("These are the utility tools available")
        time.sleep(1)
        print("01) QRcode - Generate a QR code")
        print("02) barcode - Generate a barcode")
        print("00) Return to menu.")

        tool_opt = input("Select a tool to install or run>> ")

        if tool_opt == "1" or tool_opt == "01" or tool_opt == "QRcode":
            self.install_QRcode(self.utility_menu)

        elif tool_opt == "2" or tool_opt == "02" or tool_opt == "barcode":
            self.install_barcode(self.utility_menu)

        elif tool_opt == "0" or tool_opt == "00" or tool_opt == "exit":
            self.return_to_menu(self.menu)

        else:
            print("\nPlease select a valid input, returning now.")
            self.return_to_menu(self.menu)

    # HERE WE DISPLAY THE PENTESTING MENU AND THE TOOLS
    def pentest_menu(self):
        print("These are the available tools in this CLI:\n")
        time.sleep(1)
        print("01) sqlmap - SQL injection detection and exploitation tool")
        print("02) pagodo - Google-based web vulnerability scanner")
        print("03) EmailAll - Advanced email collection tool")
        print("04) MAC_changer - Change your MAC address")
        print("00) Return to menu.")

        tool_opt = input("Select a tool to install or run>> ")

        if tool_opt == "1" or tool_opt == "01" or tool_opt == "sqlmap":
            self.install_sqlmap(self.pentest_menu)

        elif tool_opt == "2" or tool_opt == "02" or tool_opt == "pagodo":
            self.install_pagodo(self.pentest_menu)

        elif (
            tool_opt == "3"
            or tool_opt == "03"
            or tool_opt == "EmailAll"
            or tool_opt == "emailall"
        ):
            self.install_EmailAll(self.pentest_menu)

        elif (
            tool_opt == "4"
            or tool_opt == "04"
            or tool_opt == "MAC_changer"
            or tool_opt == "mac_changer"
        ):
            self.run_MAC_changer()

        if tool_opt == "00" or tool_opt == "0" or tool_opt == "back":
            self.return_to_menu(self.menu)

        else:
            print("\nPlease select a valid input, returning now.\n")
            self.return_to_menu(self.menu)

    # HERE WE DISPLAY THE MULTIPLE CALCULATION FUNCTIONS
    def calculation_menu(self):
        print("These are the available tools:\n")
        time.sleep(1)
        print("01) calculator - Simple CLI calculator")
        print("02) IMC - IMC calculator")
        print("03) watch - It gives time...")
        print("00) Return to menu")

        tool_opt = input("Select a tool to install or run>> ")

        if tool_opt == "01" or tool_opt == "1" or tool_opt.lower() == "calculator":
            self.install_calculator(self.calculation_menu)

        elif tool_opt == "02" or tool_opt == "2" or tool_opt.lower() == "imc":
            self.install_IMC(self.calculation_menu)

        elif tool_opt == "03" or tool_opt == "3" or tool_opt.lower() == "watch":
            self.install_watch(self.calculation_menu)

        elif tool_opt == "00" or "0" or "back":
            self.return_to_menu(self.calculation_menu)

        else:
            print("\nPlease select a valid input, returning now.\n")
            self.return_to_menu()
            self.calculation_menu()

    # HERE WE DISPLAY THE SETTINGS MENU
    # MOST OF THESE FUNCTIONS ARE BROKEN! SO DEAL WITH THEM CAREFULLY
    def settings_menu(self):
        print("These are the available settings:\n")
        time.sleep(1)
        print("01) Change the default directory")
        print("02) Display MAC address")
        print("00) Return to menu.")

        tool_opt = input("Please select an option\n>> ")

        if tool_opt == "01" or tool_opt == "1":
            # self.change_default_directory()
            print("This is a work in progress!")
            time.sleep(2)
            self.return_to_menu(self.menu)

        elif tool_opt == "02" or tool_opt == "2":
            print("This is a work in progress!")
            time.sleep(2)
            self.return_to_menu(self.menu)
            # self.display_MAC_address()

        elif tool_opt == "00" or tool_opt == "0":
            self.menu()

        else:
            print("\nPlease select a valid input, returning now.\n")
            self.menu()

    # THIS IS THE MAIN MENU

    def menu(self):
        print("These are the following functions:\n")
        time.sleep(1)
        print("01) Pentesting menu.")
        print("02) Calculation menu.")
        print("03) Utility menu.")
        print("99) Settings.")
        print("00) Exit CLItool")

        menu_opt = input("Select a menu to continue>> ")

        if menu_opt == "1" or menu_opt == "01" or menu_opt == "pentesting":
            os.system("clear")
            banner.test()
            self.pentest_menu()

        elif menu_opt == "2" or menu_opt == "02" or menu_opt == "calculation":
            os.system("clear")
            banner.test()
            self.calculation_menu()

        elif menu_opt == "3" or menu_opt == "03" or menu_opt == "utility":
            os.system("clear")
            banner.test()
            self.utility_menu()

        elif menu_opt == "99" or menu_opt == "settings":
            os.system("clear")
            banner.test()
            self.settings_menu()

        elif menu_opt == "0" or menu_opt == "00" or menu_opt == "exit":
            sys.exit()

        else:
            print("\nPlease select a valid input, returning now.\n")
            self.return_to_menu(self.menu)
            self.menu()


os.system("clear")
banner.test()
clitool = clitool()
clitool.menu()
