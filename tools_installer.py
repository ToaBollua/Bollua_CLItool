"""

 __     __   __     ______     ______   ______     __         __         ______     ______    
/\ \   /\ "-.\ \   /\  ___\   /\__  _\ /\  __ \   /\ \       /\ \       /\  ___\   /\  == \   
\ \ \  \ \ \-.  \  \ \___  \  \/_/\ \/ \ \  __ \  \ \ \____  \ \ \____  \ \  __\   \ \  __<   
 \ \_\  \ \_\\"\_\  \/\_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_/   \/_/ \/_/   \/_____/     \/_/   \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_/ /_/ 
                                                                                              


This script is responsible for installing, listing, and uninstalling tools.
It uses the `get_tool_info` and `get_all_tools` functions from the `tools` module to retrieve tool information.
The `install_tool` method installs a tool by name and category, and the `install_all_tools` method installs all tools in a category.
The `list_tools` and `list_installed_tools` methods list available and installed tools in a category, respectively.
The `uninstall_tool` method uninstalls a tool by name and category.

~ Bollua

"""

import os
import subprocess
import utils
from tools import get_tool_info, get_all_tools

class ToolInstaller:
    def __init__(self, base_path):
        """
        Initializes the ToolInstaller with a base path.

        Args:
            base_path (str): The base path for the tools
            will be installed. Defaults to the user's home directory.

        """
        self.base_path = base_path
        self.tools_dir = os.path.join(self.base_path, "tools")

    def install_tool(self, tool_key, category, menu):
        """Installs a tool by name and category"""
        print(f"Installing tool {tool_key} in category {category}")
        tool_info = get_tool_info(tool_key, category)
        print(f"Tool info: {tool_info}")
        if tool_info is None:
            print(f"===== Tool {tool_key} not found in category {category} ======")
            return
        
        url = tool_info.get("url")
        path = tool_info.get("path")
        tool_path = os.path.join(self.tools_dir, path)

        install_cmd = tool_info.get("install_cmd")
        if install_cmd:
            if "{name}" in install_cmd:
                if "name" not in tool_info:
                    print(f"Error: 'name' key not found in tool info for {tool_key}")
                    return
                install_cmd = install_cmd.format(name=tool_info["name"], url=url, path=tool_path)
            else:
                install_cmd = install_cmd.format(url=url, path=tool_path)



        if install_cmd is None or url is None or path is None:
            print(f"===== Tool {tool_key} is missing required information ======")
            return

        if tool_info:
            tool_path = os.path.join(self.base_path, tool_info["path"])
            if not os.path.exists(tool_path):
                print(f"===== {tool_info['name']} is not installed =====")
                print(f"===== Installing {tool_info['name']}... =====")
                try:
                    subprocess.run(tool_info["install_cmd"].format(url=tool_info["url"], path=tool_path), shell=True, check=True)
                    print(f"===== {tool_info['name']} successfully installed =====")
                    print(f"===== {tool_info['name']} is ready to use =====")
                    run_opt = input(f"Do you want to run {tool_info['name']}?\n(Y/N)>>")
                    if run_opt.lower() == "y":
                        os.system(f"cd {tool_path} && {tool_info['run_cmd']}")
                    else:
                        utils.return_to_menu(menu)
                except subprocess.CalledProcessError as e:
                    print(f"===== Error installing {tool_info['name']}: {e} =====")
            else:
                print(f"===== {tool_info['name']} is already installed =====")
                print(f"===== {tool_info['name']} is ready to use =====")
        else:
            print(f"===== Tool {tool_info['name']} not found in category {category} =====")

    def install_all_tools(self, category):
        """Installs all tools in a category"""
        tool_names = get_all_tools(category)
        for tool_key in tool_names:
            self.install_tool(tool_key, category)

    def list_tools(self, category):
        """Lists all available tools in a category"""
        tool_names = get_all_tools(category)
        print(f"Available tools in category {category}:")
        for tool_key in tool_names:
            print(tool_key)

    def list_installed_tools(self, category):
        """Lists all installed tools in a category"""
        tool_names = get_all_tools(category)
        print(f"Installed tools in category {category}:")
        for tool_key in tool_names:
            tool_info = get_tool_info(tool_key, category)
            tool_path = os.path.join(self.base_path, tool_info["path"])
            if os.path.exists(tool_path):
                print(tool_key)

    def uninstall_tool(self, tool_key, category):
        """Uninstalls a tool by name and category"""
        tool_info = get_tool_info(tool_key, category)
        if tool_info:
            tool_path = os.path.join(self.base_path, tool_info["path"])
            if os.path.exists(tool_path):
                print(f"===== Uninstalling {tool_key}... =====")
                try:
                    subprocess.run(f"rm -rf {tool_path}", shell=True, check=True)
                    print(f"===== {tool_key} successfully uninstalled =====")
                except subprocess.CalledProcessError as e:
                    print(f"===== Error uninstalling {tool_key}: {e} =====")
            else:
                print(f"===== {tool_key} is not installed =====")
        else:
            print(f"===== Tool {tool_key} not found in category {category} =====")