"""

 ______     __  __     __   __     __   __     ______     ______    
/\  == \   /\ \/\ \   /\ "-.\ \   /\ "-.\ \   /\  ___\   /\  == \   
\ \  __<   \ \ \_\ \  \ \ \-.  \  \ \ \-.  \  \ \  __\   \ \  __<   
 \ \_\ \_\  \ \_____\  \ \_\\"\_\  \ \_\\"\_\  \ \_____\  \ \_\ \_\ 
  \/_/ /_/   \/_____/   \/_/ \/_/   \/_/ \/_/   \/_____/   \/_/ /_/ 


Here is where the tools are executed!
Not very modifiable to be honest, but
it's on you to modify whatever you want!

~ Bollua      
  

"""

import os
from tools import tools
from tools_installer import ToolInstaller
from main import clitool, return_to_menu

python_command = clitool.get_python_command()

def run_tool(base_path, python_command, tool_name, menu=None):
    tool_info = tools.get(tool_name)
    if tool_info:
        tool_path = os.path.join(base_path, tool_info["path"])
        if not os.path.exists(tool_path):
            print(f"===== {tool_name} is not installed. Please install it first... =====")
            ToolInstaller.install_tool(tool_name, base_path)
        else:
            os.chdir(tool_path)
            os.system(tool_info["run_cmd"].format(path=tool_path, python_command=python_command))
            input("Press any key to continue...")
            return_to_menu(menu)
    else:
        print(f"===== Tool {tool_name} not found =====")

def run_sqlmap(base_path, python_command, menu=None):
    run_tool(base_path, python_command, "sqlmap", menu)

def run_pagodo(base_path, python_command):
    run_tool(base_path, python_command, "pagodo")

def run_EmailAll(base_path, python_command):
    run_tool(base_path, python_command, "EmailAll")

def run_calculator(base_path, python_command, menu):
    run_tool(base_path, python_command, "calculator", menu)

def run_IMC(base_path, python_command, menu):
    run_tool(base_path, python_command, "IMC", menu)

def run_watch(base_path, python_command, menu):
    run_tool(base_path, python_command, "watch", menu)

def run_QRcode(base_path, python_command, menu):
    run_tool(base_path, python_command, "qrcode", menu)

def run_barcode(base_path, python_command, menu):
    run_tool(base_path, python_command, "barcode", menu)