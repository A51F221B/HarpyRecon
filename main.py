from logging import exception
from os import execlpe
import socket
import argparse
from typing import Optional
import pyfiglet
from rich import console,status
from rich.console import group
from rich.panel import Panel

c=console.Console()

class PortScan:
    
    def __init__(self,flag):
         self.flag=flag
    
    def banner(self):
        text=pyfiglet.figlet_format("Harpy Recon")     
        c.print(text,style="bold red")
        #yield Panel(text,style="bold red")
        
        
    def ping(self,ip):
        if self.flag is True:
             c.print("[>] No Ping selected",style="bold purple")
             c.print("[+] Scanning the host",style="bold green")
             return False
        c.print("[+] Proceeding to further scan the Host",style="bold yellow")
        c.print("[+] Pinging the host",style="bold purple")
        import os
        try:
            response=os.system("ping -c1 "+ ip+" >/dev/null 2>&1")
            if response==0:
                c.print("[!] Host is online",style="bold green")
                return True
            else:
                c.print("[!] Host seems down :(",style="bold red")
                return -1
        except exception as e:
            c.print(e,style="bold red")
             
         
    def scanner(self,ip,*ports):
        if self.ping(ip)==-1:
            return
        try:
                target = socket.gethostbyname(ip)
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                for port in ports:
                        result=s.connect_ex((target,int(port)))
                        if result==0:
                            c.print(f"[+] Port {port} open",style="bold green")
                        else:
                            c.print(f"[+] Port {port} closed",style="bold red")
        except socket.error:
                c.print("[!] Server not responding",style="bold red")
                        
    
    def OsfingerPrint():
        pass

        
class Args:
    def __init__(self):
        description=c.print("Harpy - A Simple Port Scanner",style="bold red")
        self.parser=argparse.ArgumentParser(description=description)
        #self.parser.add_argument("--port","-p",dest="ports",default="1-65535",help="Defined Port range")
        self.parser.add_argument('-p',
                       '--port',
                       type=str,
                       required=True,
                       help='The specific port you want to scan')
        
        self.parser.add_argument('-ip',
                       '--address',
                       type=str,
                       required=True,
                       help='The ip address you want to scan')
        
        self.parser.add_argument('-np',
                                 '--noping',
                                 type=str,
                                 help="Directly port scanning without pinging")

        
        
# main function for testing
def main():
    flag=False
    arg=Args()
    argument=arg.parser.parse_args()

    #print(argument.noping)
    if argument.noping=='true':
          flag=True
         # print(flag)
    scanner=PortScan(flag)
    scanner.banner()
    scanner.scanner(argument.address,argument.port)
    #c.print("[!] Error in Scanning",style="bold red")
        


if __name__=='__main__':
    main()
    
    
