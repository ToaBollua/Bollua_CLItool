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

(Check the function used for git installation if you're
not on ArchLinux)

YOU CAN RUN THE MAIN.PY FILE AND GO AROUND
SOME MENUS AND FUNCTIONS, BUT THE INSTALLATION FOR
THE TOOLS IS STILL BROKEN.

I AM CURRENTLY WORKING ON MODULARIZING THE FUNCTIONS
IN THIS TOOLKIT SO ITS EASIER TO READ, UPSCALE
AND ADMINISTER IN THE FUTURE, ALSO MAKING IT
SOMEWHAT CUSTOMIZABLE FOR USERS THAT MIGHT WANNA
FORK THIS REPO AND WORK ON YOUR OWN TOOLKITS!

THANKS FOR READING AND FOR YOUR INTEREST IN MY
PROJECT! :D

~ Bollua

"""

__author__ = "Bollua"
__python_version__ = "3.12.4"

import platform
import utils
import banner
import os
import time
import menus
import shutil

class CLItool:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.python_command = utils.get_python_command()
        self.menu = menus.Menu(self.base_path, self.python_command)

    """
                 @@@@@                 
                @@@@@@@                
              @@@@@@@@@@@              
            @   @@@@@@@@@@@            
          @@@@@   @@@@@@@@@@@          
        @@@@@@@@@     @@@@@@@@@        
      @@@@@@@@@@@     @@@@@@@@@@@      
    @@@@@@@@@@@@@@      @@@@@@@@@@@    
   @@@@@@@@@@@@@@@@  @    @@@@@@@@@@   
 @@@@@@@@@@@@@@@@@@  @@@      @@@@@@@@ 
@@@@@@@@@@@@@@@@@@@  @@@@      @@@@@@@@
 @@@@@@@@@@@@@@@@@@  @@@@     @@@@@@@@ 
   @@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@   
    @@@@@@@@@@@@@@@  @@@@@@@@@@@@@@    
      @@@@@@@@@@@     @@@@@@@@@@@      
        @@@@@@@@@     @@@@@@@@@        
          @@@@@@@@@ @@@@@@@@@          
            @@@@@@@@@@@@@@@            
              @@@@@@@@@@@              Checking if git is installed and then executes a command
                @@@@@@@                in the system's command prompt or terminal to install it.
                 @@@@@                 
    """   

    def check_git_installation(self):
        if shutil.which("git") is None:
            git_opt = input("git is not installed. Do you want to install git?\n(Y/N)>> ")
            if git_opt == "Y" or git_opt == "y":
                print("===== Installing git... =====\n")
                if platform.system() == "Windows":
                    os.system("winget install --id Git.Git")
                elif platform.system() == "Darwin":  # macOS
                    os.system("brew install git")
                else:  # Linux
                    os.system("sudo pacman -S install git")  # or yum, zypper, etc. depending on the distro
                print("===== Done! =====")
            elif git_opt == "N" or git_opt == "n":
                print("Oh then fuck you...")
                self.menu.main_menu()
            else:
                print("Please insert a valid option! Exiting now. . .")
                time.sleep(3)
                os.system("clear")
                banner.test()
                return


    def run(self):
        os.system("clear")
        banner.test()
        self.check_git_installation()
        self.menu.main_menu()

if __name__ == "__main__":
    cli_tool = CLItool()
    cli_tool.run()