# THIS IS A TEST! SO TREAT THE PROGRAM AS SUCH.
# EDUCATIONAL PURPOSES ONLY! I WILL NOT BE RESPONSIBLE FOR ANY MISUSE OF THIS CODE.
# WELCOME TO YOUR WORST NIGHTMARE OF A TOOLKIT!

__author__ = "Bollua"
__python_version__ = "3.13.2" #Python version used for writing the script
                              #I recommend this version and above for the usage of the program

import sys
import os
import subprocess
import time
import shutil
import platform
import logging

try:
    import banner
except Exception as e:
    logging.error(f"[ERR] Error loading banner: {e}")

# Tool catalog. This abstracts away the need to repeat git URLs and paths.
TOOL_CATALOG = {
    "sqlmap": {
        "url": "https://github.com/sqlmapproject/sqlmap.git",
        "branch": "master",
        "category": "pentest"
    },
    "pagodo": {
        "url": "https://github.com/opsdisk/pagodo.git",
        "branch": "master",
        "category": "pentest"
    },
    "EmailAll": {
        "url": "https://github.com/Taonn/EmailAll.git",
        "branch": "master",
        "category": "pentest"
    },
    "calculator": {
        "url": "https://github.com/ToaBollua/tools4toolkit.git",
        "branch": "calculator",
        "category": "calculation"
    },
    "IMC": {
        "url": "https://github.com/ToaBollua/tools4toolkit.git",
        "branch": "IMC",
        "category": "calculation"
    },
    "watch": {
        "url": "https://github.com/ToaBollua/tools4toolkit.git",
        "branch": "time",
        "category": "calculation"
    },
    "MAC_changer": {
        "url": "https://github.com/EngineerRancho/MAC_changer.git",
        "branch": "master", # Old script didn't specify, defaulting to master
        "category": "pentest"
    },
    "QRcode": {
        "url": "https://github.com/ToaBollua/tools4toolkit.git",
        "branch": "qrcode",
        "category": "utility"
    },
    "barcode": {
        "url": "https://github.com/ToaBollua/tools4toolkit.git",
        "branch": "barcode",
        "category": "utility"
    },
    "DDoSRipper": {
        "url": "https://github.com/palahsu/DDoS-Ripper.git",
        "branch": "master",
        "category": "pentest"
    }
}

class clitool:
    def __init__(self):
        if sys.platform == "win32":
            self.base_path = os.path.join(os.getenv("USERPROFILE"), "CLItool")
        else:
            self.base_path = os.path.join(os.getenv("HOME"), ".CLItool")
        
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

        self.python_command = self.get_python_command()
        self.clear_cmd = self.get_clean_screen()
        self.check_git_installed()

    def check_git_installed(self):
        if shutil.which('git') is None:
            git_opt = input("git is not installed. Do you want to install git?\n(Y/N)>> ")
            if git_opt.lower() == "y":
                print("===== Installing git... =====\n")
                if platform.system() == 'Windows':
                    subprocess.run(['winget', 'install', '--accept-source-agreements', '--accept-package-agreements', 'Git.Git'])
                elif platform.system() == 'Darwin':
                    subprocess.run(['brew', 'install', 'git'])
                else:
                    if shutil.which('pacman'):
                        subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', 'git'])
                    elif shutil.which('apt-get'):
                        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'git'])
                    elif shutil.which('dnf'):
                        subprocess.run(['sudo', 'dnf', 'install', '-y', 'git'])
                    else:
                        print("[ERR] Could not determine Linux package manager.")
                        sys.exit(1)
                print("===== Done! =====")
            else:
                print("[!] Git is required to operate. Exiting...")
                sys.exit(1)

    def get_python_command(self):
        if shutil.which('py'): return "py"
        elif shutil.which('python3'): return "python3"
        elif shutil.which('python'): return "python"
        else:
            print("[CRITICAL] Python is not installed. Please install python 3.11.8+.")
            sys.exit(1)

    def get_clean_screen(self):
        if platform.system() == "Windows": return "cls"
        return "clear"
    
    def clean_screen(self):
        os.system(self.clear_cmd)
        print("\033[92m", end="") # Force green terminal text
        if 'banner' in sys.modules:
            banner.test()

    def get_tool_path(self, tool_name):
        return os.path.join(self.base_path, tool_name)

    def is_installed(self, tool_name):
        return os.path.exists(self.get_tool_path(tool_name))

    def install_tool(self, tool_name):
        tool_data = TOOL_CATALOG.get(tool_name)
        if not tool_data:
            print(f"[ERR] Tool {tool_name} not registered in local catalog.")
            return False

        tool_path = self.get_tool_path(tool_name)
        if self.is_installed(tool_name):
            print(f"===== {tool_name} is already installed =====")
            return True

        print(f"===== Installing {tool_name}... =====")
        branch_flag = []
        if tool_data["branch"] and tool_data["branch"] != "master":
            branch_flag = ["-b", tool_data["branch"]]
        
        cmd = ["git", "clone"] + branch_flag + [tool_data["url"], tool_path]
        result = subprocess.run(cmd)
        
        if result.returncode == 0:
            print(f"===== {tool_name} successfully installed =====")
            
            # Post-install resolving
            req_file = os.path.join(tool_path, "requirements.txt")
            if os.path.exists(req_file):
                print(f"===== Installing pip requirements for {tool_name} =====")
                subprocess.run([self.python_command, "-m", "pip", "install", "-r", req_file])
            return True
        else:
            print(f"[ERR] Kernel panic: Failed to install {tool_name}")
            return False

    def handle_tool(self, tool_name, run_func):
        if not self.is_installed(tool_name):
            if not self.install_tool(tool_name):
                input("\n[!] Press Enter to continue...")
                return
        
        run_opt = input(f"Do you want to run {tool_name} now?\n(Y/N) >> ")
        if run_opt.lower() == "y":
            run_func()
        
    def generic_run(self, tool_name, script_name="script.py"):
        tool_path = self.get_tool_path(tool_name)
        self.clean_screen()
        script_full_path = os.path.join(tool_path, script_name)
        
        if not os.path.exists(script_full_path):
            print(f"[ERR] Missing executable {script_name} in target {tool_path}")
            input("\n[!] Press Enter to continue...")
            return
            
        print(f"[SYS] Loading payload: {tool_name} -> {script_name}")
        subprocess.run([self.python_command, script_full_path], cwd=tool_path)
        input("\n[!] Press Enter to return to menu...")

    # --- Tool Specific Runners (Advanced Parameters) ---
    
    def run_sqlmap(self):
        target = input("Enter the target URL (e.g 'http[s]://target[:port]/[path/]'): ")
        if not target.strip():
            print("\033[91m[ERR] Empty target provided. Aborting.\033[92m")
            input("\n[!] Press Enter to return...")
            return
        technique = input("Enter the technique to use (e.g. -b, -t, or skip): ")
        dbms = input("Enter the DBMS (e.g. MySQL, PostgreSQL, or skip): ")
        level = input("Enter testing level (1-5, skip for default): ")
        risk = input("Enter risk (1-3, skip for default): ")
        
        cmd = [self.python_command, "sqlmap.py", "-u", target]
        if technique: cmd.extend(technique.split())
        if dbms: cmd.extend(["-d", dbms])
        if level.isdigit(): cmd.extend(["-l", level])
        if risk.isdigit(): cmd.extend(["-risk", risk])

        tool_path = self.get_tool_path("sqlmap")
        print("\n[SYS] Firing SQLmap routine...")
        subprocess.run(cmd, cwd=tool_path)
        input("\n[!] Press Enter to return...")

    def run_pagodo(self):
        domain = input("Enter the domain to search (e.g. example.com): ")
        if not domain.strip():
            print("\033[91m[ERR] Empty domain provided. Aborting.\033[92m")
            input("\n[!] Press Enter to return...")
            return
        dorks_file = input("Enter dorks file path (skip for default dorks/all_google_dorks.txt): ")
        if not dorks_file: dorks_file = "dorks/all_google_dorks.txt"
        
        max_results = input("Enter max results per dork (e.g. 10): ")
        if not max_results.isdigit(): max_results = "10"
        
        output_file = input("Save output JSON file to (optional): ")
        urls_file = input("Save URLs to text file (optional): ")
        
        cmd = [self.python_command, "pagodo.py", "-d", domain, "-g", dorks_file, "-m", max_results]
        if output_file: cmd.extend(["-o", output_file])
        if urls_file: cmd.extend(["-s", urls_file])
        
        print("\n[SYS] Initiating Google Dorks Scanner...")
        subprocess.run(cmd, cwd=self.get_tool_path("pagodo"))
        input("\n[!] Press Enter to return...")

    def run_EmailAll(self):
        print("[*] EmailAll requires certain modules. Verifying dependencies...")
        deps = ["fire", "loguru", "prettytable", "fake_useragent", "lxml"]
        for mod in deps:
            try:
                __import__(mod)
            except ImportError:
                print(f"[*] Installing missing dependency: {mod}...")
                subprocess.run([self.python_command, "-m", "pip", "install", mod.replace('_', '-')])
        
        domain = input("Enter the domain to search (e.g. example.com): ")
        cmd = [self.python_command, "emailall.py", "--domain", domain, "run"]
        print("\n[SYS] Firing EmailAll Collector...")
        subprocess.run(cmd, cwd=self.get_tool_path("EmailAll"))
        input("\n[!] Press Enter to return...")

    def run_DDoSRipper(self):
        self.clean_screen()
        target = input("Please write the target host (IP or URL)\n>> ")
        if not target.strip():
            print("\033[91m[ERR] Empty target provided. Aborting.\033[92m")
            input("\n[!] Press Enter to return...")
            return
        port = input("Please select port (Default is 22)\n>> ")
        if not port: port = "22"
        turbo = input("Please select turbo value (Default is 350)\n>> ")
        if not turbo: turbo = "350"
        
        cmd = [self.python_command, "DRipper.py", "-s", target, "-p", port, "-t", turbo]
        print("\n[SYS] Loading DDoS Ripper Payload...")
        subprocess.run(cmd, cwd=self.get_tool_path("DDoSRipper"))
        input("\n[!] Press Enter to return...")

    def is_admin(self):
        try:
            if platform.system() == "Windows":
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            else:
                return os.geteuid() == 0
        except Exception:
            return False

    def run_MAC_changer(self):
        self.clean_screen()
        if not self.is_admin():
            print("\033[91m[ERR] CRITICAL FAULT: MAC spoofing requires Administrator/Root privileges.\033[92m")
            input("\n[!] Press Enter to return...")
            return
            
        current_os = platform.system()
        print(f"[*] Detected Host OS: {current_os}")
        
        if current_os == "Windows":
            print("1) Ethernet\n2) Wi-Fi")
            net_opt = input("Select Network Type: ")
            conn = "Ethernet" if net_opt == "1" else "Wi-Fi"
            new_mac = input("Change MAC to (Format XX-XX-XX-XX-XX-XX): ")
            
            print(f"[+] Injecting new MAC {new_mac} into {conn} via netsh")
            subprocess.run(["netsh", "interface", "set", "interface", conn, "admin=disable"])
            subprocess.run(["netsh", "interface", "set", "interface", conn, "newmac=" + new_mac.replace(":", "-")])
            subprocess.run(["netsh", "interface", "set", "interface", conn, "admin=enable"])
            
        elif current_os == "Linux":
            iface = input("Interface name (e.g. eth0, wlan0): ")
            new_mac = input("Change MAC to (Format XX:XX:XX:XX:XX:XX): ")
            
            print(f"[+] Spoofing MAC on {iface} to {new_mac} via iproute2 (root required)")
            subprocess.run(["sudo", "ip", "link", "set", "dev", iface, "down"])
            subprocess.run(["sudo", "ip", "link", "set", "dev", iface, "address", new_mac])
            subprocess.run(["sudo", "ip", "link", "set", "dev", iface, "up"])
            
        else:
            print(f"[ERR] MAC changer mechanism not implemented for {current_os}.")
            
        input("\n[!] Press Enter to return...")

    def display_mac_address(self):
        self.clean_screen()
        current_os = platform.system()
        print(f"[*] Fetching MAC addresses for {current_os} interfaces...\n")
        if current_os == "Windows":
            subprocess.run(["getmac", "/v"])
        elif current_os == "Linux":
            subprocess.run(["ip", "link"])
        elif current_os == "Darwin":
             subprocess.run(["ifconfig"])
        input("\n[!] Press Enter to return...")

    def change_default_directory(self):
        self.clean_screen()
        print(f"[*] Current Clone Directory: {self.base_path}")
        new_dir = input("Enter new absolute path for tool cloning (or press Enter to cancel):\n>> ")
        if new_dir.strip():
            new_dir = os.path.expanduser(new_dir.strip())
            if os.path.exists(new_dir) and os.path.isdir(new_dir):
                self.base_path = new_dir
                print(f"[+] Default directory successfully updated to: {self.base_path}")
            else:
                mk_opt = input("[?] Directory does not exist. Create it? (Y/N) >> ")
                if mk_opt.lower() == 'y':
                    try:
                        os.makedirs(new_dir)
                        self.base_path = new_dir
                        print(f"[+] Created and set new directory: {self.base_path}")
                    except Exception as e:
                        print(f"[ERR] Failed to create directory: {e}")
                else:
                    print("[-] Operation cancelled.")
        input("\n[!] Press Enter to return...")

    # --- Subsystem Menus (Loop-based, Memory Safe) ---

    def utility_menu(self):
        while True:
            self.clean_screen()
            print("----- UTILITY MENU -----")
            print("01) QRcode  - Generate a QR code string")
            print("02) barcode - Generate a barcode sequence")
            print("00) Back to Kernel Root")
            
            opt = input(">> ")
            if opt in ["1", "01", "QRcode"]:
                self.handle_tool("QRcode", lambda: self.generic_run("QRcode"))
            elif opt in ["2", "02", "barcode"]:
                self.handle_tool("barcode", lambda: self.generic_run("barcode"))
            elif opt in ["0", "00", "back"]:
                break
            else:
                input("[!] Invalid instruction. Press Enter.")

    def pentest_menu(self):
         while True:
            self.clean_screen()
            print("----- PENTEST MENU -----")
            print("01) sqlmap      - SQL injection automated scanner")
            print("02) pagodo      - Google dorks scraper")
            print("03) EmailAll    - Email discovery engine")
            print("04) MAC_changer - Universal MAC Spoofer (Host script)")
            print("05) DDoSRipper  - Network stress tester")
            print("00) Back to Kernel Root")
            
            opt = input(">> ")
            if opt in ["1", "01"]:
                self.handle_tool("sqlmap", self.run_sqlmap)
            elif opt in ["2", "02"]:
                self.handle_tool("pagodo", self.run_pagodo)
            elif opt in ["3", "03"]:
                self.handle_tool("EmailAll", self.run_EmailAll)
            elif opt in ["4", "04"]:
                # The old code ran an external python script for mac changer but we've internalized it
                self.run_MAC_changer()
            elif opt in ["5", "05"]:
                self.handle_tool("DDoSRipper", self.run_DDoSRipper)
            elif opt in ["0", "00", "back"]:
                break
            else:
                input("[!] Invalid instruction. Press Enter.")

    def calculation_menu(self):
        while True:
            self.clean_screen()
            print("----- CALCULATION MENU -----")
            print("01) calculator - Simple CLI calculator string")
            print("02) IMC        - Body Mass Index algorithm")
            print("03) watch      - Active time terminal widget")
            print("00) Back to Kernel Root")
            
            opt = input(">> ")
            if opt in ["1", "01"]:
                self.handle_tool("calculator", lambda: self.generic_run("calculator"))
            elif opt in ["2", "02"]:
                self.handle_tool("IMC", lambda: self.generic_run("IMC"))
            elif opt in ["3", "03"]:
                self.handle_tool("watch", lambda: self.generic_run("watch"))
            elif opt in ["0", "00", "back"]:
                break
            else:
                input("[!] Invalid instruction. Press Enter.")

    def settings_menu(self):
         while True:
            self.clean_screen()
            print("----- SYSTEM SETTINGS -----")
            print("01) Change Default Clone Directory")
            print("02) Display interface MAC adresses")
            print("00) Back to Kernel Root")
            
            opt = input(">> ")
            if opt in ["1", "01"]:
                self.change_default_directory()
            elif opt in ["2", "02"]:
                self.display_mac_address()
            elif opt in ["0", "00", "back"]:
                break
            else:
                input("[!] Invalid instruction. Press Enter.")

    def menu(self):
        while True:
            self.clean_screen()
            print("----- ROOT TERMINAL -----")
            print("01) Pentesting Subsystem")
            print("02) Calculation Subsystem")
            print("03) Utility Subsystem")
            print("99) System Settings")
            print("00) Terminate Kernel")
            
            opt = input(">> ")
            if opt in ["1", "01"]:
                self.pentest_menu()
            elif opt in ["2", "02"]:
                self.calculation_menu()
            elif opt in ["3", "03"]:
                self.utility_menu()
            elif opt in ["99"]:
                self.settings_menu()
            elif opt in ["0", "00", "exit"]:
                self.clean_screen()
                print("[SYS] Disconnecting modules. Terminal session closed.")
                sys.exit(0)
            else:
                input("[!] Command unrecognized. Press Enter.")

if __name__ == "__main__":
    try:
        app = clitool()
        app.menu()
    except KeyboardInterrupt:
        os.system("cls" if platform.system() == "Windows" else "clear")
        print("\n\033[91m[SYS_FAULT] KeyboardInterrupt detected. Shutting down Kernel...\033[0m")
        sys.exit(0)
