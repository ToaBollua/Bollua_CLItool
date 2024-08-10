# CLItool

CLItool is a multipurpose, menu-driven tool that allows you to easily install and run various projects from GitHub, including personal productivity tools and pentesting tools. It is designed for personal use and educational purposes.

### Features

* **Easy Installation**: Install projects from GitHub with a single command. This feature saves you time and effort by automating the installation process.
* **Menu-Driven Interface**: Navigate through menus to select tools, and CLItool will take care of the rest. This intuitive interface makes it easy to use, even for those who are new to command-line tools.
* **Modular Design**: CLItool is designed to be modular, making it easy to read, upscale, and administer in the future. It's also somewhat customizable for users who might want to fork this repo and work on their own toolkits.
* **Utility Functions**: CLItool includes a set of utility functions in the `utils.py` file, which can be imported and used in other scripts. These functions provide helpful tools for tasks such as determining the Python command to use.
* **Tool Management**: The `tools.py` file contains a dictionary of tools, organized by category, which can be easily expanded or modified by adding or modifying tool entries.
* **Tool Installer**: The `tool_installer.py` file provides a `ToolInstaller` class that allows you to install, list, and uninstall tools. This class provides a convenient way to manage tools and makes it easy to add new tools to the system.

**Important Note**: Please use CLItool responsibly and at your own risk. I am not responsible for any misuse of the program.

### Inspiration and Goals

CLItool is inspired by other projects like Babymux, but it runs the programs it installs by itself, without the need for the user to manually run them. This makes it a convenient and time-saving solution for users.

### Current Status

This branch of the CLItool toolkit is made for Linux (might make it universal later). The installation for the tools is currently broken, but you can still run the main.py file and explore the menus and functions.

### System Requirements

* Python 3.11.8 or later (recommended)
* Linux (currently designed to work mainly on Linux)
* Git (will be installed automatically if not already installed)

### Installation Instructions

1. Clone this repository: `git clone https://github.com/ToaBollua/Bollua_CLItool.git`
2. Execute the main.py file with Python: `python main.py`
3. Follow the menus and instructions to install and run the tools.

**Note**: If you're not on ArchLinux or you don't have the 'pacman' package manager, you might need to modify the function used for git installation to your package manager command.

### Menu Structure

The menus are structured as follows:

* **Main Menu**: The main menu provides options to navigate to different categories of tools, including Penetration Testing Tools, Calculation Tools, and Utility Tools.
* **Category Menus**: Each category menu displays a list of available tools in that category. You can select a tool to install or run, or return to the main menu.
* **Tool Selection**: After selecting a tool, you can choose to install or run it. The tool will be installed if it's not already installed, and then it will be run.

### Tool Management

The `tools.py` file contains a dictionary of tools, organized by category, which can be easily expanded or modified by adding or modifying tool entries. The dictionary includes the following categories:

* **Pentest**: Tools for penetration testing, including sqlmap, pagodo, and emailall.
* **Calculation**: Tools for calculations, including a simple calculator, IMC calculator, and a watch tool.
* **Utility**: Tools for generating QR codes and barcodes.

The `tool_installer.py` file provides a `ToolInstaller` class that allows you to:

* **Install a tool**: Use the `install_tool` method to install a tool by name and category.
* **Install all tools in a category**: Use the `install_all_tools` method to install all tools in a category.
* **List available tools in a category**: Use the `list_tools` method to list all available tools in a category.
* **List installed tools in a category**: Use the `list_installed_tools` method to list all installed tools in a category.
* **Uninstall a tool**: Use the `uninstall_tool` method to uninstall a tool by name and category.

### Contributing

I am open to any push requests, issues, or feedback you may have about this project. Please be respectful and constructive in your feedback.

If you have any tool suggestions, I'd be glad to read them out!!

~ Bollua