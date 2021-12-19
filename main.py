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
    
    def banner(self):
        text=pyfiglet.figlet_format("Harpy Recon")     
        c.print(text,style="bold red")
        #yield Panel(text,style="bold red")
        
        
        
    def ping(self,ip):
        c.print("[+] Pinging the host",style="bold purple")
        import os
        try:
            response=os.system("ping -c1 "+ ip+" >/dev/null 2>&1")
            if response==0:
                c.print("[+] Host is online",style="bold green")
                return True
            else:
                c.print("[+] Host seems down :(",style="bold red")
        except exception as e:
            c.print(e,style="bold red")
             
         
    def scanner(self,ip,*ports):
        if(self.ping(ip)):
            c.print("[+] Proceeding to further scan the Host",style="bold green")
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
                c.print("[+] Server not responding",style="bold red")
                        
    
    def OsfingerPrint():
        pass
        
        
class Args:
    def __init__(self):
        self.parser=argparse.ArgumentParser(description="Harpy - A Simple Port Scanner")
        #self.parser.add_argument("--port","-p",dest="ports",default="1-65535",help="Defined Port range")
        self.parser.add_argument('--port',
                       metavar='port',
                       type=str,
                       required=True,
                       help='The specific port you want to scan')
        
        self.parser.add_argument('--ip',
                       metavar='ip',
                       type=str,
                       required=True,
                       help='The ip address you want to scan')
        
        self.parser.add_argument('--noping',
                                 metavar='noping',
                                 type=str,
                                 help="Directly port scanning without pinging")

        
        
# main function for testing
def main():
    #ip="192.168.8.100"
    #port=8080,22
    scanner=PortScan()
    scanner.banner()
    arg=Args()
    argument=arg.parser.parse_args()
    #scanner.scanner(ip,port)
    #scanner.ping('192.168.8.102')
    #parser=argparse.ArgumentParser(description="Harpy - A Simple Port Scanner")
    #parser.add_argument("--port",dest="ports",default="1-65535",help="Defined Port range")
    #args=parser.parse_args()
    try:
       print(argument.ip)
       scanner.scanner(argument.ip,argument.port)
    except:
        c.print("[!] Error in Scanning",style="bold red")
        


if __name__=='__main__':
    main()