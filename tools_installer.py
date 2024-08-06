"""

 __     __   __     ______     ______   ______     __         __         ______     ______    
/\ \   /\ "-.\ \   /\  ___\   /\__  _\ /\  __ \   /\ \       /\ \       /\  ___\   /\  == \   
\ \ \  \ \ \-.  \  \ \___  \  \/_/\ \/ \ \  __ \  \ \ \____  \ \ \____  \ \  __\   \ \  __<   
 \ \_\  \ \_\\"\_\  \/\_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_/   \/_/ \/_/   \/_____/     \/_/   \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_/ /_/ 
                                                                                              

Here is where the tools are installed!
Not very modifiable to be honest, but
it's on you to modify whatever you want!

~ Bollua

"""

import os
import subprocess
from tools import get_tool_info, get_all_tools

class ToolInstaller:
    def __init__(self, base_path):
        self.base_path = base_path

    def install_tool(self, tool_name, category):
        """Installs a tool by name and category"""
        tool_info = get_tool_info(category, tool_name)
        if tool_info is None:
            print(f"===== Tool {tool_name} not found in category {category} ======")
            return
        
        install_cmd = tool_info.get("install_cmd")
        url = tool_info.get("url")
        path = tool_info.get("path")

        if install_cmd is None or url is None or path is None:
            print(f"===== Tool {tool_name} is missing required information ======")
            return

        if tool_info:
            tool_path = os.path.join(self.base_path, tool_info["path"])
            if not os.path.exists(tool_path):
                print(f"===== {tool_name} is not installed =====")
                print(f"===== Installing {tool_name}... =====")
                try:
                    subprocess.run(tool_info["install_cmd"].format(url=tool_info["url"], path=tool_path), shell=True, check=True)
                    print(f"===== {tool_name} successfully installed =====")
                    print(f"===== {tool_name} is ready to use =====")
                except subprocess.CalledProcessError as e:
                    print(f"===== Error installing {tool_name}: {e} =====")
            else:
                print(f"===== {tool_name} is already installed =====")
                print(f"===== {tool_name} is ready to use =====")
        else:
            print(f"===== Tool {tool_name} not found in category {category} =====")

    def install_all_tools(self, category):
        """Installs all tools in a category"""
        tool_names = get_all_tools(category)
        for tool_name in tool_names:
            self.install_tool(tool_name, category)

    def list_tools(self, category):
        """Lists all available tools in a category"""
        tool_names = get_all_tools(category)
        print(f"Available tools in category {category}:")
        for tool_name in tool_names:
            print(tool_name)

    def list_installed_tools(self, category):
        """Lists all installed tools in a category"""
        tool_names = get_all_tools(category)
        print(f"Installed tools in category {category}:")
        for tool_name in tool_names:
            tool_info = get_tool_info(tool_name, category)
            tool_path = os.path.join(self.base_path, tool_info["path"])
            if os.path.exists(tool_path):
                print(tool_name)

    def uninstall_tool(self, tool_name, category):
        """Uninstalls a tool by name and category"""
        tool_info = get_tool_info(tool_name, category)
        if tool_info:
            tool_path = os.path.join(self.base_path, tool_info["path"])
            if os.path.exists(tool_path):
                print(f"===== Uninstalling {tool_name}... =====")
                try:
                    subprocess.run(f"rm -rf {tool_path}", shell=True, check=True)
                    print(f"===== {tool_name} successfully uninstalled =====")
                except subprocess.CalledProcessError as e:
                    print(f"===== Error uninstalling {tool_name}: {e} =====")
            else:
                print(f"===== {tool_name} is not installed =====")
        else:
            print(f"===== Tool {tool_name} not found in category {category} =====")