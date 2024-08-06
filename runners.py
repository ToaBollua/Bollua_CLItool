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
import subprocess
from tools import tools
from tools_installer import ToolInstaller
from utils import get_python_command

python_command = get_python_command()

tool_runners = {(category, tool_name): lambda base_path, python_command, menu=None: run_tool(base_path, python_command, category, tool_name, menu) for category, tools_in_category in tools.items() for tool_name in tools_in_category}

def run_tool(base_path: str, python_command: str, category: str, tool_name: str, menu=None) -> None:
    """Runs a tool by name and category"""
    tool_path = os.path.join(base_path, category, tool_name)
    if os.path.exists(tool_path):
        subprocess.run([python_command, tool_path])
    else:
        print(f"===== Tool {tool_name} not found in category {category} =====")

def run_tool_by_name(base_path: str, python_command: str, tool_name: str, menu=None) -> None:
    """Runs a tool by name"""
    for (category, name), tool_runner in tool_runners.items():
        if name == tool_name:
            tool_runner(base_path, python_command, menu)
            return
    print(f"===== Tool {tool_name} not found =====")