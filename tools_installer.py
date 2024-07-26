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
from tools import tools

class ToolInstaller:
    def __init__(self, base_path, urls):
        self.base_path = base_path

    def install_tool(self, tool_name):
        tool_info = tools.get(tool_name)
        if tool_info:
            tool_path = os.path.join(self.base_path, tool_info["path"])
            if not os.path.exists(tool_path):
                print(f"===== {tool_name} is not installed =====")
                print(f"===== Installing {tool_name}... =====")
                os.system(tool_info["install_cmd"].format(url=tool_info["url"], path=tool_path))
                print(f"===== {tool_name} successfully installed =====")
                print(f"===== {tool_name} is ready to use =====")
            else:
                print(f"===== {tool_name} is already installed =====")
                print(f"===== {tool_name} is ready to use =====")
        else:
            print(f"===== Tool {tool_name} not found =====")
      

    """
    _ _ _ ____ ____ _  _ _ _  _ ____   /
    | | | |__| |__/ |\ | | |\ | | __  / 
    |_|_| |  | |  \ | \| | | \| |__] .  

    In case you wanna install all tools
    just put this function outside the
    docstring.

    def install_all_tools(self):
        for tool in tools:
        self.install_tool(tool_name)

    """