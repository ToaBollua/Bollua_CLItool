"""


 __  __     ______   __     __         ______    
/\ \/\ \   /\__  _\ /\ \   /\ \       /\  ___\   
\ \ \_\ \  \/_/\ \/ \ \ \  \ \ \____  \ \___  \  
 \ \_____\    \ \_\  \ \_\  \ \_____\  \/\_____\ 
  \/_____/     \/_/   \/_/   \/_____/   \/_____/ 
                                                 

This script handles utility functions so they
can be imported and called later.

You can add functions here if you want and then
call them later in other scripts, even in other
projects if you want ;)

~ Bollua

"""


import shutil



def get_python_command():
    if shutil.which("py") is not None:
        return "py"
    elif shutil.which("python") is not None:
        return "python"
    elif shutil.which("python3") is not None:
        return "python3"
    else:
        print("Python is not installed. Please install python and try again.\n===== RECOMMENDED VERSION 3.11.8 =====")
        return None
    

def return_to_menu(menu):
    input("Press Enter to return to the menu...")
    menu()


