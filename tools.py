"""

 ______   ______     ______     __         ______    
/\__  _\ /\  __ \   /\  __ \   /\ \       /\  ___\   
\/_/\ \/ \ \ \/\ \  \ \ \/\ \  \ \ \____  \ \___  \  
   \ \_\  \ \_____\  \ \_____\  \ \_____\  \/\_____\ 
    \/_/   \/_____/   \/_____/   \/_____/   \/_____/ 
                                                     

This is the tool dictionary.
It contains all the tools that are used in the program.

You can expand or modify the tools just by
adding or modifying the functions in this file.

Happy hacking!
~ Bollua

"""


from main import get_python_command

tools = {
    "sqlmap": {
        "name": "sqlmap",
        "description": "SQL injection detection and exploitation tool",
        "url": "https://github.com/sqlmapproject/sqlmap.git",
        "path": "sqlmap",
        "install_cms": "git clone {url} {path}",
        "run_cmd": "python {path}/sqlmap.py"
},

    "pagodo": {
        "name": "pagodo",
        "description": "Google-based web vulnerability scanner",
        "url": "https://github.com/opsdisk/pagodo.git",
        "path": "pagodo",
        "install_cmd": "git clone {url} {path}",
        "run_cmd": "python {path}/pagodo.py"
},
    "emailall": {
        "name": "EmailAll",
        "description": "Advanced email collection tool",
        "url": "https://github.com/Taonn/EmailAll.git",
        "path": "emailall",
        "install_cmd": "git clone {url} {path}",
        "run_cmd": "python {path}/emailall.py"
},
    "calculator": {
        "name": "calculator",
        "description": "Simple calculator",
        "url": "https://github.com/ToaBollua/tools4toolkit.git",
        "path": "calculator",
        "install_cmd": "git clone -b {name} {url} {path}",
        "run_cmd": "python {path}/calculator.py"
},
    "IMC": {
        "name": "IMC",
        "description": "IMC Calculator script",
        "url": "https://github.com/ToaBollua/tools4toolkit.git",
        "path": "IMC",
        "install_cmd": "git clone -b {name} {url} {path}",
        "run_cmd": "python {path}/IMC.py"
},
    "watch": {
        "name": "watch",
        "description": "It... gives time.",
        "url": "https://github.com/ToaBollua/tools4toolkit.git",
        "path": "watch",
        "install_cmd": "git clone -b {name} {url} {path}",
        "run_cmd": "python {path}/watch.py"
},
    "qrcode": {
        "name": "QRcode",
        "description": "QRcode generator",
        "url": "https://github.com/ToaBollua/tools4toolkit.git",
        "path": "qrcode",
        "install_cmd": "git clone -b {name} {url} {path}",
        "run_cmd": "python {path}/qrcode.py"
},
    "barcode": {
        "name": "Barcode",
        "description": "Barcode generator",
        "url": "https://github.com/ToaBollua/tools4toolkit.git",
        "path": "barcode",
        "install_cmd": "git clone -b {name} {url} {path}",
        "run_cmd": "python {path}/barcode.py"
}

}

def get_tool_info(tool_name):
    return tools.get(tool_name)

def get_all_tools():
    return list(tools.keys())

def add_tool(tool_name, tool_info):
    tools[tool_name] = tool_info
