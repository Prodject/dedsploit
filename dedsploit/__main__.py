#!/usr/bin/env python3
import os
import sys
import platform

from .modules import http, net, smtp
from .consts import ColorScheme as col

MODULES = {
    "http":     ["slowloris"],
    "net":      ["arpspoof", "pscan", "hosts"],
    "smtp":     ["smsbomb"]
}


HEADER = C + """
    .___         .___             .__         .__  __
  __| _/____   __| _/____________ |  |   ____ |__|/  |_
 / __ |/ __ \ / __ |/  ___/\____ \|  |  /  _ \|  \   __|
/ /_/ \  ___// /_/ |\___ \ |  |_> >  |_(  <_> )  ||  |
\____ |\___  >____ /____  >|   __/|____/\____/|__||__|
     \/    \/     \/    \/ |__|
\n""" + W


VERSION = LG + """\n
         [   Version: 3.0.0                     ]
         [   Modules: %s                         ]\n""" % len(MODULES) + W


HELP_OPTIONS = [
    ("help", "Display available commands and modules"),
    ("modules", "Show modules that can be used"),
    ("clear", "Move the screen up to clear it"),
    ("update", "Update dedsploit!"),
    ("exit", "Exit the program or current module"),
    ("use ...", "Select a module for use")
]


def print_command_help(command_help):
    """
    unpacks each list, and create a help menu
    """
    help_map = dict(command_help)
    for h in help_map:
        print("{0}\t\t\t{1}".format(h, help_map[h]) + W)


def get_key(value):
    """
    returns values from each sublist within a dict
    """
    return next(key for key, lst in MODULES.iteritems() for item in lst if item == value)


def main():

    # check platform
    if platform.system() != "Linux":
        print(R + "[!] You are not using Linux! dedsploit may not work! [!]" + W)

    # print HEADER and info
    print(HEADER, VERSION)
    print(LC + "For available commands, type 'help'.\nFor available modules, enter 'modules'. Exit with Ctrl + C or 'exit'.\n")

    # input loop
    while True:
        options = raw_input(LP + "[>>] " + W )

        if options == "help":
            print(f"{LR}\n[Commands Available:]\n{LG}")
            print_command_help(help_options)
            continue

        elif options == "modules":
            print(LR + "\n[There are currently " + LP + "{}".format(sum(len(lst) for lst in MODULES.values())) + LR + " modules available:]\n" + LG)
            for protocol, module_list in MODULES.items():
                for mod in module_list:
                    print("{}\t\t({})\n".format(str(mod), str(protocol)))
            continue

        elif options.startswith("use"):

            # return a list of all concatenated sublists
            modname = options.split()[1]
            mod_list = [name for lst in MODULES.values() for name in lst]
            if modname in mod_list:
                print(LISTMSG)
                protocol = get_key(modname)
                if protocol == "http":
                    http.HTTP(modname).execute()
                elif protocol == "net":
                    net.Net(modname).execute()
                elif protocol == "smtp":
                    smtp.SMTP(modname).execute()
            else:
                print(WARNING)

        elif options == "clear":
            os.system("clear")
            continue

        elif options == "exit":
            break

        else:
            print(WARNING)
            continue


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(LR + "\n[!] Goodbye! Remember to Hack the Gibson!" + W)
        exit()
    except IndexError:
        print(R + "[!] Module not found! [!]" + W)
