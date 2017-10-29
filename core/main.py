import os, sys, threading, signal, socket
import smtplib, logging, random, platform, subprocess
import nmap, readline

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
 
from time import sleep
from getpass import getpass
from subprocess import call
from scapy.all import *
from scapy.error import Scapy_Exception

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
LR = '\033[1;31m' # light red
LG = '\033[1;32m' # light green
LO = '\033[1;33m' # light orange
LB = '\033[1;34m' # light blue
LP = '\033[1;35m' # light purple
LC = '\033[1;36m' # light cyan

lan_ip = os.popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'").read()
public_ip = os.popen("wget http://ipinfo.io/ip -qO -").read()
if platform.system() == "Darwin":
	mac_address = os.popen("ifconfig en1 | awk '/ether/{print $2}'").read()
	gateway_ip = os.popen("netstat -nr | grep default | grep -oE '\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b'").read()
else:
	mac_address = os.popen("cat /sys/class/net/eth0/address").read()
	gateway_ip = os.popen("/sbin/ip route | awk '/default/ { printf $3 }'").read()

WARNING = R + "Not recognized!" + W
LISTMSG =  LC + "Type 'list' to show all of available attack vectors" + W

def print_command_help(command_help):
    print LR + ("\n[Commands Available:]\n""") + LG
    help_map = dict(command_help)
    for h in help_map:
        print "{0}\t\t\t{1}".format(h, help_map[h])
    print "\n" + W

help_options = [
    ("help", "Display available commands and modules"),
    ("modules", "Show modules that can be used"),
    ("clear", "Move the screen up to clear it"),
    ("update", "Update dedsploit!"),
    ("exit", "Exit the program or current module"),
    ("use ...", "Select a module for use")
]

slowloris_menu = [
    ("target <ip>", "Set the target's IP address"),
    ("connections <number>", "Set the number of connections to send"),
    ("length <time>", "Time to keep attack alive"),
    ("start", "Start the attack"),
]

smsbomb_menu = [
    ("target <phone>", "Set the target's phone number"),
    ("carrier <carrier>", "Set the target's phone carrier (use list carriers to show)"),
    ("email <email>", "Set disposable email WITHOUT @email identifier"),
    ("list carriers", "List available carriers"),
    ("start", "Start the attack"),
]

pscan_menu = [
    ("scan <ip>", "Portscan on IP address"),
]

arpspoof_menu = [
    ("target <ip> ", "Set the target's IP address"),
    ("packet <count>", "Set number of packets to send"),
    ("start", "Start the attack"),
]