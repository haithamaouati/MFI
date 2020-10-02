# Author: HawkHA

import os

print("""
 ___  _________ _____ 
 |  \/  ||  ___|_   _|
 | .  . || |_    | |  
 | |\/| ||  _|   | |  by HawkHA
 | |  | || |    _| |_ 
 \_|  |_/\_|    \___/ 
""")

print("Metasploit-Framework Install")
print("[*] Installing ... \n")
os.system("apt update && apt upgrade -y && apt isntal git -y && apt install curl -y")
os.system("curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh")
os.system("chmod +x metasploit.sh")
os.system("./metasploit.sh")
print("\n")
print("[*] Installation finished.")
print("[*] Launch Metasploit-Framework ... \n")
os.system("msfconsole")