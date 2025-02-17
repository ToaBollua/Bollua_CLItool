# THIS IS A TEST! SO TREAT THE PROGRAM AS SUCH.
# EDUCATIONAL PURPOSES ONLY! I WILL NOT BE RESPONSIBLE FOR ANY MISUSE OF THIS CODE.
# WELCOME TO YOUR WORST NIGHTMARE OF A TOOLKIT!


__author__ = "Bollua"
__python_version__ = "3.13.1" #Python version used for writing the script
                              #I recommend this version and above for the usage of the program

# IMPORTS SCRIPT'S DEPENDENCIES
try:
    import sys
    import os
    import subprocess
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
    

# HERE GOES THE TOOLS GITHUB LINKS
class clitool:
    def __init__(self):
#      ______  ___ _____ _   _ 
#      | ___ \/ _ \_   _| | | |
#      | |_/ / /_\ \| | | |_| |
#      |  __/|  _  || | |  _  |
#      | |   | | | || | | | | |
#      \_|   \_| |_/\_/ \_| |_/                        
# 
#       HERE WE DEFINE THE PATH AND TELL THE PROGRAM
#       TO USE THE USER'S HOME DIRECTORY 
#       TRY NOT TO TOUCH THIS PART
#       UNLESS YOU KNOW WHAT YOU'RE DOING OFC!

        if sys.platform == "win32":
            self.base_path = os.path.join(os.getenv("USERPROFILE"), "CLItool")
        else:
            self.base_path = os.path.join(os.getenv("HOME"), ".CLItool")
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

#       NOW THIS SECTION IS FOR SPECIFYING EACH TOOL DIRECTORY NAME
#       THIS CAN BE OPTIMIZED (PRETTY MUCH LIKE THE WHOLE SCRIPT)
#       BUT I DO NOT RECOMMEND MESSING WITH THIS BLOCK OF CODE
#       FEEL FREE TO ADD YOUR OWN TOOLS HERE THO, MAKE SURE TO
#       USE THE SAME SYNTAX AS THE BLOCK BELOW!!!

        self.sqlmap_path = os.path.join(self.base_path, "sqlmap")
        self.pagodo_path = os.path.join(self.base_path, "pagodo")
        self.EmailAll_path = os.path.join(self.base_path, "EmailAll")
        self.calculator_path = os.path.join(self.base_path, "calculator")
        self.IMC_path = os.path.join(self.base_path, "IMC")
        self.watch_path = os.path.join(self.base_path, "watch")
        self.MAC_changer_path = os.path.join(self.base_path, "MAC_changer")
        self.QRcode_path = os.path.join(self.base_path, "QRcode")
        self.barcode_path = os.path.join(self.base_path, "barcode")
        self.DDoSRipper_path = os.path.join(self.base_path, "DDoSRipper")
        
#       TOOLS GITHUB DOWNLOAD URL SO WE CAN CALL THEM LATER
#       PRETTY MUCH THE SAME AS ABOVE HERE, I DO NOT RECOMMEND
#       CHANGING HOW THIS WORKS UNLESS YOU KNOW WHAT YOU'RE DOING
#       BUT YOU MUST ADD THE GIT REPOSITORY'S LINK HERE, DEFINING
#       IT AS YOUR TOOL'S URL, AS SHOWN BELOW

        self.sqlmap_url = 'https://github.com/sqlmapproject/sqlmap.git'
        self.pagodo_url = 'https://github.com/opsdisk/pagodo.git'
        self.EmailAll_url = 'https://github.com/Taonn/EmailAll.git'
        self.calculator_url = 'https://github.com/ToaBollua/tools4toolkit.git'
        self.IMC_url = 'https://github.com/ToaBollua/tools4toolkit.git'
        self.watch_url = 'https://github.com/ToaBollua/tools4toolkit.git'
        self.MAC_changer_url = 'https://github.com/EngineerRancho/MAC_changer.git'
        self.QRcode_url = 'https://github.com/ToaBollua/tools4toolkit.git'
        self.barcode_url = 'https://github.com/ToaBollua/tools4toolkit.git'
        self.DDoSRipper_url = 'https://github.com/palahsu/DDoS-Ripper.git'
        
#       THIS SETS YOUR DEFAULT PYTHON COMMAND AFTER CHECKING
#       DO NOT DELETE ;)

        self.python_command = self.get_python_command()
       
#        _____ _____ _____ 
#       |  __ \_   _|_   _|
#       | |  \/ | |   | |  
#       | | __  | |   | |  
#       | |_\ \_| |_  | |  
#        \____/\___/  \_/  
#
#       CHECK IF REQUIREMENTS ARE MET
#       THE GIT CHECKING SEQUENCE OF CODE
#       DOES NOT WORK AS INTENDED, FEEL FREE
#       TO TRY AND FIX IT IF YOU WANT
#       YOU CAN ADD OTHER PACKAGE MANAGERS
#       OR OTHER STUFF FOR IT

        if shutil.which('git') is None:
            self.git_opt = input("git is not installed. Do you want to install git?\n(Y/N)>> ")
            if self.git_opt == "Y" or self.git_opt == "y":
                print("===== Installing git... =====\n")
                if platform.system() == 'Windows':
                    os.system('winget install --id Git.Git')
                elif platform.system() == 'Darwin':  # macOS
                    os.system('brew install git')
                else:  # Linux
                    os.system('sudo apt-get install git')  # or yum, zypper, etc. depending on the distro
                print("===== Done! =====")
            elif self.git_opt == "N" or self.git_opt == "n":
                print("Oh then fuck you...")
                self.return_to_menu(menu)
            else:
                print("Please insert a valid option! Exiting now. . .")
                time.sleep(3)
                os.system(get_clean_screen())
                banner.test()
                return

# THIS CHECKS WHICH PYTHON COMMAND IS USED IN THE USER'S MACHINE AND USES THAT TO OPEN OTHER PYTHON FILES
    def get_python_command(self):
        if shutil.which('py') is not None:
            return "py"
        elif shutil.which('python') is not None:
            return "python"
        elif shutil.which("python3") is not None:
            return "python3"
        else:
            print("Python is not installed. Please install python and try again.\n===== RECOMMENDED VERSION 3.11.8 =====")
    
            
#       ADDS REQUIREMENTS TO THE SYSTEM'S PATH ENVIROMENT VARIABLE
#       I AM HONESTLY NOT SURE IF THIS BLOCK OF CODE IS USEFUL OR NOT
#       IT'S SUPPOSED TO ADD GIT TO THE ENVIROMENT VARIABLE IF IT'S NOT
#       INSTALLED, BUT APPARENTLY ONLY WORKS ON LINUX.
#       REVIEW LATER!!!

        if 'git' not in os.environ['PATH']:
            os.environ['PATH'] += os.pathsep + '/usr/bin'

#   ALMOST THE SAME AS THE GET PYTHON COMMAND BUT FOR CLEANING
#   THE USER'S SCREEN FOR DIFFERENT OS

    def get_clean_screen(self):
        if shutil.which('cls') is not None:
            return "cls"
        elif shutil.which('clear') is not None:
            return "clear"
        else:
            print("Clean screen command not found. Please check 'get_clean_screen' function.")
            return

#   PERSONALLY MY FAVOURITE FUNCTION OF THIS WHOLE
#   SCRIPT! IS SO SIMPLE YET SO USEFUL!
#   BUT YEAH... IT JUST RETURNS THE USER TO THE MENU

    def return_to_menu(self, menu):
        print("Returning to main menu...")
        os.system(self.get_clean_screen())
        time.sleep(1)
        banner.test()
        self.menu()

#   ▪   ▐ ▄ .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▌  ▄▄▌  ▄▄▄ .▄▄▄  .▄▄ · 
#   ██ •█▌▐█▐█ ▀. •██  ▐█ ▀█ ██•  ██•  ▀▄.▀·▀▄ █·▐█ ▀. 
#   ▐█·▐█▐▐▌▄▀▀▀█▄ ▐█.▪▄█▀▀█ ██▪  ██▪  ▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄
#   ▐█▌██▐█▌▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█▌▐▌▐█▌▐▌▐█▄▄▌▐█•█▌▐█▄▪▐█
#   ▀▀▀▀▀ █▪ ▀▀▀▀  ▀▀▀  ▀  ▀ .▀▀▀ .▀▀▀  ▀▀▀ .▀  ▀ ▀▀▀▀ 
#   
#   HERE ARE ALL THE INSTALLATION FUNCTIONS
#   FOR EVERY TOOL IN THE PROGRAM!!!
#   I KNOW THIS METHOD OF WRITING THE FUNCTIONS
#   IS REPETITIVE, HARD TO READ AND ALL
#   I'M WORKING ON IT ON SEPARATE BRANCHES
#   FEEL FREE TO TRY AND IMPLEMENT A SOLUTION
#   BY YOURSELF!
#   IF YOU DARE c:<
        
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
            os.system(f"{self.python_command} -m pip uninstall holehe --yes")
            os.system(f"{self.python_command} -m pip install -e {holehe_path}")
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
            os.system(f"{self.python_command} -m pip install -r requirements.txt")
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
            os.system(f"{self.python_command} -m pip install -r requirements.txt")
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
            os.system(f"git clone -b calculator {self.calculator_url} {calculator_path}")
            print("===== calculator succesfully installed =====")
            print("===== calculator is ready to use =====")
            run_opt = input("Do you want to run calculator?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_calculator()
            else:
                self.return_to_menu(menu)
    
    def install_IMC(self, menu):
        IMC_path = os.path.join(self.base_path, "IMC")
        if os.path.exists(IMC_path):
            print("===== IMC is already installed =====")
            print("===== IMC is ready to use =====")
            run_opt = input("Do you want to run IMC?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_IMC()
            else:
                self.return_to_menu(menu)
        
        else:
            print("===== IMC is not installed =====")
            print("===== Installing IMC... =====")
            os.system(f"git clone -b IMC {self.IMC_url} {IMC_path}")
            print("===== IMC succesfully installed =====")
            print("===== IMC is ready to use =====")
            run_opt = input("Do you want to run IMC?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_IMC()
            else:
                self.return_to_menu(menu)
                
    def install_watch(self, menu):
        watch_path = os.path.join(self.base_path, "watch")
        if os.path.exists(watch_path):
            print("===== watch is already installed =====")
            print("===== watch is ready to use =====")
            run_opt = input("Do you want to run watch?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_watch()
            else:
                self.return_to_menu(menu)
                
        else:
            print("===== watch is not installed =====")
            print("===== installing watch... =====")
            os.system(f"git clone -b time {self.watch_url} {watch_path}")
            print("===== watch succesfully installed =====")
            print("===== watch is ready to use =====")
            run_opt = input("Do you want to run watch?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_watch()
            else:
                self.return_to_menu(menu)
    
    def install_MAC_changer(self, menu):
        MAC_changer_path = os.path.join(self.base_path, "MAC_changer")
        if os.path.exists(MAC_changer_path):
            print("===== MAC_changer is already installed =====")
            print("===== MAC_changer is ready to use =====")
            run_opt == input("Do you want to run MAC_changer?/n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_MAC_changer()
            else:
                self.return_to_menu(menu)
        
        else:
            print("===== MAC_changer is not installed. =====")
            print("===== Installing MAC_changer... =====")
            os.system(f"git clone {self.MAC_changer_url} {self.MAC_changer_path}")
            print("===== MAC_changer succesfully installed =====")
            print("===== MAC_changer is ready to use =====")
            run_opt = input("Do you want to run MAC_changer?\n(Y/N)\n>> ")
            if run_opt.lower() == 'y':
                self.run_MAC_changer()
            else:
                self.retun_to_menu(menu)

    def install_QRcode(self, menu):
        QRcode_path = os.path.join(self.base_path, "QRcode")
        if os.path.exists(QRcode_path):
            print("===== QRcode is already installed =====")
            print("===== QRcode is ready to use =====")
            run_opt = input("Do you want to run QRcode?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_QRcode()
            else:
                self.return_to_menu(menu)
                
        else:
            print("===== QRcode is not installed =====")
            print("===== Installing QRcode... =====")
            os.system(f"git clone -b qrcode {self.QRcode_url} {QRcode_path}")
            print("===== QRcode succesfully installed =====")
            print("===== QRcode is ready to use =====")
            run_opt = input("Do you want to run QRcode?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_QRcode()
            else:
                self.return_to_menu(menu)
                
    def install_barcode(self, menu):
        barcode_path = os.path.join(self.base_path, "barcode")
        if os.path.exists(barcode_path):
            print("===== barcode is already installed =====")
            print("===== barcode is ready to use =====")
            run_opt = input("Do you want to run barcode?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_barcode()
            else:
                self.return_to_menu(menu)
                
        else:
            print("===== barcode is not installed =====")
            print("===== Installing barcode... =====")
            os.system(f"git clone -b barcode {self.barcode_url} {barcode_path}")
            print("===== barcode succesfully installed =====")
            print("===== barcode is ready to use =====")
            run_opt = input("Do you want to run barcode?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_barcode()
            else:
                self.return_to_menu(menu)

    def install_DDoSRipper(self, menu):
        DDoSRipper_path = os.path.join(self.base_path, "DDoSRipper")
        if os.path.exists(DDoSRipper_path):
            print("===== DDoSRipper is already installed =====")
            print("===== DDoSRipper is ready to use =====")
            run_opt = input("Do you want to run DDoSRipper?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_DDoSRipper()
            else:
                self.return_to_menu(menu)
        else:
            print("===== DDoSRipper is not installed =====")
            print("===== Installing DDoSRipper... =====")
            os.system(f"git clone {self.DDoSRipper_url} {DDoSRipper_path}")
            print("===== DDoSRipper succesfully installed =====")
            print("==== DDoSRipper is ready to use =====")
            run_opt = input("Do you want to run DDoSRipper?\n(Y/N)\n>> ")
            if run_opt.lower() == "y":
                self.run_DDoSRipper()
            else:
                self.return_to_menu(menu)


#   ▄▄▄  ▄• ▄▌ ▐ ▄  ▐ ▄ ▄▄▄ .▄▄▄  .▄▄ · 
#   ▀▄ █·█▪██▌•█▌▐█•█▌▐█▀▄.▀·▀▄ █·▐█ ▀. 
#   ▐▀▀▄ █▌▐█▌▐█▐▐▌▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄
#   ▐█•█▌▐█▄█▌██▐█▌██▐█▌▐█▄▄▌▐█•█▌▐█▄▪▐█
#   .▀  ▀ ▀▀▀ ▀▀ █▪▀▀ █▪ ▀▀▀ .▀  ▀ ▀▀▀▀ 
#   HERE LAY ALL THE RESPECTIVE
#   RUN FUNCTIONS FOR EVERY TOOL
#   MOST RUN FUNCTIONS ARE UNIQUE TO
#   IT'S TOOL, SINCE THE IDEA OF THE
#   TOOLKIT IS TO ABSTRACT THE NEED
#   OF FLAG USAGE AND TURN IT INTO
#   A MENU WITH OPTIONS FOR COMMON
#   USE OR, IDEALLY, ALL THE TOOL'S
#   FUNCTIONS
    
    def run_sqlmap(self, menu=None):
        # PROMPT THE USER FOR SQLMAP OPTIONS AND EXECUTE THEM
        target = input("Enter the target URL (e.g 'http[s]://target[:port]/[path/]'): ")
        technique = input("Enter the technique to use (e.g. -b for boolean-based blind, -t for time-based, etc.): ")
        dbms = input("Enter the DBMS (e.g. MySQL, PostgreSQL, etc.): ")
        level = input("Enter the level of testing (1-5, where 1 is the least intrusive and 5 is the most intrusive): ")
        risk = input("Enter the risk (1-3, where 1 is the least risky and 3 is the most risky): ")
        try:
            level = int(level)
            risk = int(risk)
        except ValueError:
            print("Invalid input. Please enter a number for the level and risk.\n")
            return

        # CHANGE TO THE SQLMAP DIRECTORY
        os.chdir(os.path.join(self.base_path, "sqlmap"))
        os.system(f"{self.python_command} sqlmap.py -u {target} {technique} -d {dbms} -l {level} -risk {risk}")
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
            
            command = f"{self.python_command} pagodo.py -d {domain} -g {dorks_file} -m {max_results}"
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
            command = f"{self.python_command} emailall.py --domain {domain} run"
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while process.poll() is None:
                quit_command = input("Enter 'q' to quit the program: ")
                if quit_command.lower() == 'q':
                    process.terminate()
                    break
            os.system(command)
            input("Press any key to continue...\n")
            self.return_to_menu(self.menu)
            
    # THIS FUNCTION IS SPECIAL BECAUSE IT'S SUPPOSED TO WORK EVEN WITHOUT A GITHUB REPO.
    def run_MAC_changer(self):
        os.system("cls")
        banner.test()
        network_type = int(input("Network Type (1 for Ethernet, 2 for Wi-Fi): "))
        if network_type == 1:
            connection = "Ethernet"
        elif network_type == 2:
            connection = "Wi-Fi"
        else:
            print("Invalid network type. Please select 1 or 2.")
            
        new_mac = input("Change the MAC address to (format: XX-XX-XX-XX-XX-XX): ")
            
        print("[+] Changing the MAC address to " + new_mac)
        os.system("netsh interface set interface " + connection + " admin=disable")
        os.system("netsh interface set interface " + connection + " admin=enable")
        os.system("netsh interface set interface " + connection + " newmac=" + new_mac.replace(":", "-"))
        os.system("netsh interface show interface " + connection)
            
                
    
    def run_calculator(self):
        calculator_path = os.path.join(self.base_path, "calculator")
        if not os.path.exists(calculator_path):
            print("===== calculator is not installed. Please install it first... =====")
            self.install_calculator(self.calculation_menu)
        else:
            os.chdir(calculator_path)
            os.system("cls")
            banner.test()
            os.system(f"{self.python_command} script.py")
            input("Press any key to continue...")
            self.return_to_menu(self.calculation_menu)
    
    def run_IMC(self):
        IMC_path = os.path.join(self.base_path, "IMC")
        if not os.path.exists(IMC_path):
            print("===== IMC is not installed. Please install it first... =====")
            self.install_IMC(self.calculation_menu)
        else:
            os.chdir(IMC_path)
            os.system("cls")
            banner.test()
            os.system(f"{self.python_command} script.py")
            input("Press any key to continue...")
            self.return_to_menu(self.calculation_menu)
    
    def run_watch(self):
        watch_path = os.path.join(self.base_path, "watch")
        if not os.path.exists(watch_path):
            print("===== watch is not installed. Please install it first... =====")
            self.install_watch(self.calculation_menu)
        else:
            os.chdir(watch_path)
            os.system("cls")
            banner.test()
            os.system(f"{self.python_command} script.py")
            input("Press any key to continue...")
            self.return_to_menu(self.calculation_menu)       
        
    def run_MAC_changer(self):
        MAC_changer_path = os.path.join(self.base_path, "MAC_changer")
        if not os.path.exists(MAC_changer_path):
            print("===== MAC_changer is not installed. Please install it first... =====")
            self.install_MAC_changer(self.calculation_menu)
        else:
            os.chdir(MAC_changer_path)
            os.system("cls")
            banner.test()
            os.system(f"{self.python_command} MAC_windows.py")
            input("Press any key to continue...")
            self.return_to_menu(self.pentest_menu)

    def run_QRcode(self):
        QRcode_path = os.path.join(self.base_path, "QRcode")
        if not os.path.exists(QRcode_path):
            print("===== QRcode is not installed. Please install it first... =====")
            self.install_QRcode(self.calculation_menu)
        else:
            os.chdir(QRcode_path)
            os.system("cls")
            banner.test()
            os.system(f"{self.python_command} script.py")
            input("Press any key to continue...")
            self.return_to_menu(self.calculation_menu)    
    
    def run_barcode(self):
        barcode_path = os.path.join(self.base_path, "barcode")
        if not os.path.exists(barcode_path):
            print("===== barcode is not installed. Please install it first... =====")
            self.install_barcode(self.calculation_menu)
        else:
            os.chdir(barcode_path)
            os.system("cls")
            banner.test()
            os.system(f"{self.python_command} script.py")
            input("Press any key to continue...")
            self.return_to_menu(self.calculation_menu)

    def run_DDoSRipper(self):
        DDoSRipper_path = os.path.join(self.base_path, "DDoSRipper")
        if not os.path.exists(DDoSRipper_path):
            print("===== DDoSRipper is not installed. Please install it first... =====")
            self.install_DDoSRipper(self.pentest_menu)
        else:
            os.chdir(DDoSRipper_path)
            os.system(self.get_clean_screen())
            banner.test()
            target = input("Please write the target host (IP or URL)\n>> ")
            port = input("Please select port (Default is 22)\n>> ")
            turbo = input("Please select turbo value (Default is 350)\n>> ")
            os.system(f"{self.python_command} DRipper.py -s {target} -p {port} -t {turbo}")
            self.return_to_menu(self.menu)
            
# HERE ARE THE SETTINGS FUNCTIONS
    def change_default_directory(self): # NEED FIXING
        new_dir = input("Enter the new defaullt directory: ")
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            self.base_path = new.dir
            print("Default directory changed successfully!")
            print(f"Default directory changed to {new_dir}")
            input("Press any key to continue...")
            self.return_to_menu(self.menu)
        else:
            print("The directory you entered does not exist or is not a directory.")
            input("Press any key to continue...")
            self.return_to_menu(self.menu)
    
    def display_MAC_address(self): # NEED FIXING
        network_type = int(input("Network Type (1 for Ethernet, 2 for Wi-Fi): "))
        if network_type == 1:
            connection = "Ethernet"
        elif network_type == 2:
            connection = "Wi-Fi"
        else:
            print("Invalid network type. Please select 1 or 2.")
            return

        if connection == "Ethernet":
            mac_address = subprocess.check_output(["getmac", "/v", connection]).decode().split("\n")[1].split()[-1]
        else:
            output = subprocess.check_output(["netsh", "interface", "show", "interface"]).decode()
            if "Wi-Fi" in output:
                mac_address = output.split("Wi-Fi")[1].split("\n")[1].split(":")[1].strip()
            else:
                print("Wi-Fi interface not found.")
                return

        print("The MAC address of", connection, "is", mac_address)

#    • ▌ ▄ ·. ▄▄▄ . ▐ ▄ ▄• ▄▌.▄▄ · 
#   ·██ ▐███▪▀▄.▀·•█▌▐██▪██▌▐█ ▀. 
#   ▐█ ▌▐▌▐█·▐▀▀▪▄▐█▐▐▌█▌▐█▌▄▀▀▀█▄
#   ██ ██▌▐█▌▐█▄▄▌██▐█▌▐█▄█▌▐█▄▪▐█
#   ▀▀  █▪▀▀▀ ▀▀▀ ▀▀ █▪ ▀▀▀  ▀▀▀▀        
#   FROM HERE YOU WILL FIND THE MUTIPLE
#   MENUS AVAILABLE FOR THE TOOLKIT!
#   FEEL FREE TO ADD MORE MENUS AS YOU NEED
#   TO. JUST REMEMBER TO ADD THEM TO THE
#   MAIN MENU!!!


#   THIS IS THE UTILITY MENU
#   USED FOR UTILITY TOOLS
#   LIKE CALCULATORS, GRAPHIC TOOLS
#   AND OTHER MISCELLANEOUS SCRIPTS
    def utility_menu(self):
        print("These are the utility tools available")
        time.sleep(1)
        print("01) QRcode - Generate a QR code")
        print("02) barcode - Generate a barcode")
        
        tool_opt = input("Select a tool to install or run>> ")
        
        if tool_opt == "1" or tool_opt == "01" or tool_opt == "QRcode":
            self.install_QRcode(self.utility_menu)
        
        elif tool_opt == "2" or tool_opt == "02" or tool_opt == "barcode":
            self.install_barcode(self.utility_menu)
            
        else:
            print("\nPlease select a valid input, returning now.")
            self.return_to_menu(self.menu)

#   HERE WE DISPLAY THE PENTESTING MENU AND THE TOOLS    
    def pentest_menu(self):
        print("These are the available tools in this CLI:\n")
        time.sleep(1)
        print("01) sqlmap - SQL injection detection and exploitation tool")
        print("02) pagodo - Google-based web vulnerability scanner")
        print("03) EmailAll - Advanced email collection tool")
        print("04) MAC_changer - Change your MAC address")
        print("05) DDoSRipper - DDoS tool (Please make sure you are anon first)")
        print("00) Return to menu.")
    
        tool_opt = input("Select a tool to install or run>> ")
    
        if tool_opt == "1" or tool_opt == "01" or tool_opt == "sqlmap":
            self.install_sqlmap(self.pentest_menu)
        
        elif tool_opt == "2" or tool_opt == "02" or tool_opt  == "pagodo":
            self.install_pagodo(self.pentest_menu)
        
        elif tool_opt == "3" or tool_opt == "03" or tool_opt == "EmailAll" or tool_opt == "emailall":
            self.install_EmailAll(self.pentest_menu)
            
        elif tool_opt == "4" or tool_opt == "04" or tool_opt == "MAC_changer" or tool_opt == "mac_changer":
            self.run_MAC_changer()

        elif tool_opt == "5" or tool_opt == "05" or tool_opt == "DDoSRipper" or tool_opt == "ddosripper":
              self.run_DDoSRipper()
        

        if tool_opt == "00" or tool_opt == "0" or tool_opt == "back":
            self.return_to_menu(self.menu)
            
        else:
            print("\nPlease select a valid input, returning now.\n")
            self.return_to_menu(self.menu)

#   HERE WE DISPLAY THE MULTIPLE CALCULATION FUNCTIONS
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
        
#   HERE WE DISPLAY THE SETTINGS MENU
#   MOST OF THESE FUNCTIONS ARE BROKEN! SO DEAL WITH THEM CAREFULLY
    def settings_menu(self):
        print("These are the available settings:\n")
        time.sleep(1)
        print("01) Change the default directory")
        print("02) Display MAC address")
        print("00) Return to menu.")
        
        tool_opt = input("Please select an option\n>> ")
        
        if tool_opt == "01" or tool_opt == "1":
            #self.change_default_directory()
            print("This is a work in progress!")
            time.sleep(2)
            self.return_to_menu(self.menu)
        
        elif tool_opt == "02" or tool_opt == "2":
            print("This is a work in progress!")
            time.sleep(2)
            self.return_to_menu(self.menu)
            #self.display_MAC_address()
        
        elif tool_opt == "00" or tool_opt == "0":
            self.retunr_to_menu(self.menu())
        
        else:
            print("\nPlease select a valid input, returning now.\n")
            self.return_to_menu(self.menu())
            self.settings_menu()
            
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
            os.system(self.get_clean_screen())
            banner.test()
            self.pentest_menu()
            
        elif menu_opt == "2" or menu_opt == "02" or menu_opt == "calculation":
            os.system(self.get_clean_screen())
            banner.test()
            self.calculation_menu()
        
        elif menu_opt == "3" or menu_opt == "03" or menu_opt == "utility":
            os.system(self.get_clean_screen())
            banner.test()
            self.utility_menu()
            
        elif menu_opt == "99" or menu_opt == "settings":
            os.system(self.get_clean_screen())
            banner.test()
            self.settings_menu()
        
        elif menu_opt == "0" or menu_opt == "00" or menu_opt == "exit":
            sys.exit()
        
        else:
            print("\nPlease select a valid input, returning now.\n")
            self.return_to_menu(self.menu)
            self.menu()


os.system(clitool.get_clean_screen(clitool))
banner.test()
clitool = clitool()
clitool.menu()
