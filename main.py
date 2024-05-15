# THIS IS A TEST! SO TREAT THE PROGRAM AS SUCH.
# EDUCATIONAL PURPOSES ONLY! I WILL NOT BE RESPONSIBLE FOR ANY MISUSE OF THIS CODE.

__author__ = "Bollua"
__python_version__ = "3.11.8"


try:
    import sys
    import os
    import subprocess
    import winreg
    import time
    import shutil
    import banner
    import logging
except Exception as e:
    logging.error(e)

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
        if sys.platform == "win32":
            self.base_path = os.path.join(os.getenv("USERPROFILE"), "CLItool")
        else:
            self.base_path = os.path.join(os.getenv("HOME"), ".CLItool")
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
        self.sqlmap_path = os.path.join(self.base_path, "sqlmap")
        self.pagodo_path = os.path.join(self.base_path, "pagodo")
        self.EmailAll_path = os.path.join(self.base_path, "EmailAll")
        self.calculator_path = os.path.join(self.base_path, "calculator")
        
        # TOOLS GITHUB DOWNLOAD URL SO WE CAN CALL THEM LATER
        self.sqlmap_url = 'https://github.com/sqlmapproject/sqlmap.git'
        self.pagodo_url = 'https://github.com/opsdisk/pagodo.git'
        self.EmailAll_url = 'https://github.com/Taonn/EmailAll.git'
        self.calculator_url = 'https://github.com/ToaBollua/Calculadora.git'
        
        
        
        #CHECK IF REQUIREMENTS ARE MET
        if shutil.which('git') is None:
            self.git_opt = input("git is not installed. Do you want to install git?\n(Y/N)>> ")
            if git_opt == "Y" or self.git_opt == "y":
                print("===== Installing git... =====\n")
                os.system('py -m pip install git')
                print("===== Done! =====")
            elif self.git_opt == "N" or self.git_opt == "n":
                print("Oh then fuck you...")
                self.return_to_menu(menu)
            else:
                print("Please insert a valid option! Exiting now. . .")
                time.sleep(3)
                os.system("cls")
                banner.test()
                return
            
    # ADDS REQUIREMENTS TO THE SYSTEM'S PATH ENVIROMENT VARIABLE
        if 'git' not in os.environ['PATH']:
            os.environ['PATH'] += os.pathsep + '/usr/bin'
    
    def return_to_menu(self, menu):
        print("Returning to main menu...")
        time.sleep(3)
        os.system("cls")
        banner.test()
        self.menu()

    # HERE WE INSTALL THE TOOLS
        
    def install_sqlmap(self, menu):
        sqlmap_path = os.path.join(self.base_path, "sqlmap")
        if os.path.exists(sqlmap_path):
            print("===== sqlmap is already installed. =====")
            print("===== sqlmap is ready to use. =====")
            run_opt = input("Do you want to run sqlmap?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_sqlmap()
            else:
                self.return_to_menu(menu)
        else:
            print("===== sqlmap is not installed. =====")
            print("===== Installing sqlmap... =====")
            os.system(f"git clone {self.sqlmap_url} {sqlmap_path}")
            print("===== sqlmap succesfully installed. =====")
            print("===== sqlmap is ready to use. =====")
            run_opt = input("Do you want to run sqlmap?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_sqlmap(menu)
            else:
                self.return_to_menu(menu)
            
    def install_holehe(self, menu):
        holehe_path = os.path.join(self.base_path, "holehe")
        if os.path.exists(holehe_path):
            print("===== holehe is already installed. =====")
            print("===== holehe is ready to use. =====")
            self.run_holehe(menu)
        else:
            print("===== holehe is not installed. =====")
            print("===== Installing holehe... =====")
            os.system(f"git clone {self.holehe_url} -b master --single-branch --depth 1 {holehe_path}")
            os.chdir(holehe_path)
            os.system("py -m pip uninstall holehe --yes")
            os.system(f"py -m pip install -e {holehe_path}")
            os.chdir(self.base_path)
            print("===== holehe succesfully installed. =====")
            print("===== holehe is ready to use. =====")
            run_opt = input("Do you want to run holehe?\n(Y/N)\n>> ").lower()
            if run_opt == "y":
                run_holehe(menu)
            else:
                self.return_to_menu(menu)
    
    def install_pagodo(self, menu):
        pagodo_path = os.path.join(self.base_path, "pagodo")
        if os.path.exists(pagodo_path):
            print("===== pagodo is already installed. =====")
            print("===== pagodo is ready to use. =====")
            run_opt = input("Do you want to run pagodo?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_pagodo()
                self.return_to_menu(menu)
            else:
                self.return_to_menu(menu)
        else:
            print("===== pagodo is not installed. =====")
            print("===== Installing pagodo... =====")
            os.system(f"git clone {self.pagodo_url} -b master --single-branch --depth 1 {pagodo_path}")
            print("===== Installing pagodo requirements... =====")
            os.chdir(pagodo_path)
            os.system("py -m pip install -r requirements.txt")
            os.chdir(self.base_path)
            print("===== pagodo requirements successfully installed. =====")
            print("===== pagodo succesfully installed. =====")
            print("===== pagodo is ready to use. =====")
            run_opt = input("Do you want to run pagodo?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_pagodo()
            else:
                self.return_to_menu(menu)
                
    def install_EmailAll(self, menu):
        EmailAll_path = os.path.join(self.base_path, "EmailAll")
        if os.path.exists(EmailAll_path):
            print("===== EmailAll is already installed. =====")
            print("===== EmailAll is ready to use. =====")
            run_opt = input("Do you want to run EmailAll?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_EmailAll()
                self.return_to_menu(menu)
            else:
                self.return_to_menu(menu)
        else:
            print("===== EmailAll is not installed. =====")
            print("===== Installing EmailAll... =====")
            os.system(f"git clone {self.EmailAll_url} {EmailAll_path}")
            print("===== Installing EmailAll requirements... =====")
            os.chdir(EmailAll_path)
            os.system("py -m pip install -r requirements.txt")
            print("===== EmailAll succesfully installed. =====")
            print("===== EmailAll is ready to use. =====")
            run_opt = input("Do you want to run EmailAll?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_EmailAll()
            else:
                self.return_to_menu(menu)
    
    def install_calculator(self, menu):
        calculator_path = os.path.join(self.base_path, "calculator")
        if os.path.exists(calculator_path):
            print("===== calculator is already installed =====")
            print("===== calculator is ready to use =====")
            run_opt = input("Do you want to run calculator?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_calculator()
            else:
                self.return_to_menu(menu)
                
        else:
            print("===== calculator is not installed =====")
            print("===== Installing calculator... =====")
            os.system(f"git clone -b master {self.calculator_url} {calculator_path}")
            print("===== calculator succesfully installed =====")
            print("===== calculator is ready to use =====")
            run_opt = input("Do you want to run calculator?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_calculator()
            else:
                self.return_to_menu(menu)


# HERE WE RUN THE TOOLS
    
    def run_sqlmap(self):
        # PROMPT THE USER FOR SQLMAP OPTIONS AND EXECUTE THEM
        target = input("Enter the target URL (e.g 'http[s]://target[:port]/[path/]'): ")
        technique = input("Enter the technique to use (e.g. -b for boolean-based blind, -t for time-based, etc.): ")
        dbms = input("Enter the DBMS (e.g. MySQL, PostgreSQL, etc.): ")
        level = input("Enter the level of testing (1-5): ")
        risk = input("Enter the risk (1-3): ")
        try:
            level = int(level)
            risk = int(risk)
        except ValueError:
            print("Invalid input. Please enter a number for the level and risk.\n")
            return

        # CHANGE TO THE SQLMAP DIRECTORY
        os.chdir(os.path.join(self.base_path, "sqlmap"))
        os.system(f"py sqlmap.py -u {target} {technique} -d {dbms} -l {level} -risk {risk}")
        input("Press any key to continue...")
        self.return_to_menu(menu)

    def run_pagodo(self):
        pagodo_path = os.path.join(self.base_path, "pagodo")
        if not os.path.exists(pagodo_path):
            print("===== pagodo is not installed. Please install it first. =====")
            self.install_pagodo(menu)
        else:
            os.chdir(pagodo_path)
            domain = input("Enter the domain to search (e.g. example.com): ")
            dorks_file = input("Enter the path to the dorks file (e.g. dorks/all_google_dorks.txt)\nYou can skip this if you don't have any dork file: ")
            if not dorks_file:
                dorks_file = "dorks/all_google_dorks.txt"
            max_results = int(input("Enter the maximum number of results to return per dork (e.g. 10): "))
            output_file = input("Enter the path to save the output JSON file (optional): ")
            urls_file = input("Enter the path to save the URLs to a text file (optional): ")
            
            command = f"py pagodo.py -d {domain} -g {dorks_file} -m {max_results}"
            if output_file:
                command += f" -o {output_file}"
            if urls_file:
                command += f" -s {urls_file}"
            
            os.system(command)
            input("Press any key to continue...\n")
    
    # IMPORTANT! EMAILALL IS SHOWING ERRORS WHILE RUNNING BUT IT SOMEHOW WORKS...
    # NEED TO FIX THIS LATER... maybe.
    def run_EmailAll(self):
        EmailAll_path = os.path.join(self.base_path, "EmailAll")
        if not os.path.exists(EmailAll_path):
            print("===== EmailAll is not installed. Please install it first. =====")
            self.install_EmailAll(menu)
        else:
            os.chdir(EmailAll_path)
            try:
                import fire
                import loguru
                import prettytable
                import fake_useragent
                import lxml
            except ModuleNotFoundError:
                print("===== Some modules not found. Installing modules... =====")
                os.system("py -m pip install fire")
                os.system("py -m pip install loguru")
                os.system("py -m pip install prettytable")
                os.system("py -m pip install fake_useragent")
                os.system("py -m pip install lxml")
            domain = input("Enter the domain to search (e.g. example.com): ")
            command = f"py emailall.py --domain {domain} run"
            os.system(command)
            input("Press any key to continue...\n")
    
    def run_calculator(self):
        calculator_path = os.path.join(self.base_path, "calculator")
        if not os.path.exists(calculator_path):
            print("===== calculator is not installed. Please install it first... =====")
            self.install_calculator(self.calculation_menu)
        else:
            os.chdir(calculator_path)
            os.system("cls")
            banner.test()
            os.system(f"py Calculadora4.8.py")
            input("Press any key to continue...")
            self.return_to_menu(self.calculation_menu)


    def delete_tools(self):
        print("===== Deleting tools... =====")
        for dir in ["calculator", "EmailAll", "pagodo", "sqlmap", "__pycache__"]:
            dir_path = os.path.join(self.base_path, dir)
            if os.path.exists(dir_path):
                try:
                    subprocess.run(["rmdir", "/s", "/q", dir_path], shell=True)
                    print(f"Deleted {dir_path}")
                except OSError as e:
                    print(f"Error deleting {dir_path}: {e}")
        print("===== Tools deleted. =====")
        
            

# HERE WE DISPLAY THE PENTESTING MENU AND THE TOOLS    
    def pentest_menu(self):
        print("These are the available tools in this CLI:\n")
        time.sleep(1)
        print("01) sqlmap - SQL injection detection and exploitation tool")
        print("02) pagodo - Google-based web vulnerability scanner")
        print("03) EmailAll - Advanced email collection tool")
        print("00) Return to menu.")
    
        tool_opt = input("Select a tool to install or run>> ")
    
        if tool_opt == "1" or tool_opt == "01" or tool_opt == "sqlmap":
            self.install_sqlmap(self.pentest_menu)
        
        elif tool_opt == "2" or tool_opt == "02" or tool_opt  == "pagodo":
            self.install_pagodo(self.pentest_menu)
        
        elif tool_opt == "3" or tool_opt == "03" or tool_opt == "EmailAll" or tool_opt == "emailall":
            self.install_EmailAll(self.pentest_menu)
        

        if tool_opt == "00" or tool_opt == "0" or tool_opt == "back":
            self.return_to_menu(self.menu)
            
        else:
            print("\nPlease select a valid input, returning now.\n")
            time.sleep(3)
            os.system("cls")
            banner.test()
            self.menu()

# HERE WE DISPLAY THE MULTIPLE CALCULATION FUNCTIONS
    def calculation_menu(self):
        print("These are the available tools:\n")
        time.sleep(1)
        print("01) calculator - Simple CLI calculator")
        print("00) Return to menu")
        
        tool_opt = input("Select a tool to install or run>> ")
        
        if tool_opt == "01" or "1" or "calculator":
            self.install_calculator(self.calculation_menu)
        
        elif tool_opt == "00" or "0" or "back":
            self.return_to_menu()
        
# HERE WE DISPLAY THE SETTINGS MENU
    def settings_menu(self):
        print("These are the available settings:\n")
        time.sleep(1)
        print("01) Change the default directory (WIP)")
        print("02) Delete tools (For update purposes) (WIP)")
        print("00) Return to menu.")
        
        tool_opt = input("Please select an option\n>> ")
        
        if tool_opt == "01" or tool_opt == "1":
            print("This is a work in progress!")
            self.return_to_menu(self.menu)
        
        elif tool_opt == "02" or tool_opt == "2":
            #self.delete_tools()
            print("This is a work in progress!")
            self.return_to_menu(self.menu)
        
        elif tool_opt == "00" or tool_opt == "0":
            self.return_to_menu(self.menu)
        
        else:
            print("\nPlease select a valid input, returning now.\n")
            time.sleep(3)
            os.system("cls")
            banner.test()
            self.settings_menu()
            
# THIS IS THE MAIN MENU

            
    def menu(self):
        print("These are the following functions:\n")
        time.sleep(1)
        print("01) Pentesting menu.")
        print("02) Calculation menu.")
        print("99) Settings.")
        print("00) Exit CLItool")
        
        menu_opt = input("Select a menu to continue>> ")
        
        if menu_opt == "1" or menu_opt == "01" or menu_opt == "pentesting":
            os.system("cls")
            banner.test()
            self.pentest_menu()
            
        elif menu_opt == "2" or menu_opt == "02" or menu_opt == "calculation":
            os.system('cls')
            banner.test()
            self.calculation_menu()
            
        elif menu_opt == "99" or menu_opt == "settings":
            os.system("cls")
            banner.test()
            self.settings_menu()
        
        elif menu_opt == "0" or menu_opt == "00" or menu_opt == "exit":
            sys.exit()
        
        else:
            print("\nPlease select a valid input, returning now.\n")
            time.sleep(3)
            os.system("cls")
            banner.test()
            self.menu()


os.system("cls")
banner.test()
clitool = clitool()
clitool.menu()