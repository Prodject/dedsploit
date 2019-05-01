"""
consts.py

Defines global module-wide constants to be used
during execution
"""

class ColorScheme:
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


    WARNING = R + "Not recognized!" + W
    LISTMSG =  LC + "Type 'list' to show all of available attack vectors" + W


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
